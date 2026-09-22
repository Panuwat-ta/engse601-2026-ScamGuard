"""Week 06 integration probes against the frozen ENGSE212 main baseline.

Run from the extracted baseline server directory with the project Python 3.10 venv.
External DB/Redis/model services are replaced only at explicit integration seams.
"""
from __future__ import annotations

import json
import os
import sys
import types
import uuid
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock

# Safe test-only configuration. No production secret or database is read.
os.environ.setdefault("ALLOWED_ORIGINS", "http://localhost")
os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://w06:w06@127.0.0.1:5432/w06")
os.environ.setdefault("JWT_SECRET_KEY", "week06-test-only-key")
os.environ.setdefault("REDIS_URL", "redis://127.0.0.1:6379/15")
os.environ.setdefault("ONNX_MODEL_PATH", "/tmp/w06-missing.onnx")
os.environ.setdefault("XAI_MODEL_PATH", "/tmp/w06-missing.gguf")
os.environ.setdefault("LOCAL_UPLOAD_DIR", "/tmp/w06-api-uploads")
os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("CUDA_VISIBLE_DEVICES", "")
Path(os.environ["LOCAL_UPLOAD_DIR"]).mkdir(parents=True, exist_ok=True)

# Prevent expensive model initialization while retaining the real scan-service seam.
class StubInference:
    def __init__(self):
        self.calls = 0
        self.raise_exc = False
        self.result = {
            "visual_risk_score": 60,
            "ai_gen_probability": 0.60,
            "heatmap_bytes": b"",
            "ocr_text": "",
            "anomaly_region": "test region",
        }

    def predict(self, _image_bytes: bytes) -> dict:
        self.calls += 1
        if self.raise_exc:
            raise RuntimeError("forced inference failure")
        return dict(self.result)

    def generate_xai_explanation(self, **_kwargs) -> str:
        return "test-only explanation"

stub_inference = StubInference()
stub_mod = types.ModuleType("app.services.inference_service")
stub_mod.inference_service = stub_inference
sys.modules["app.services.inference_service"] = stub_mod

import io
import pytest
from httpx import ASGITransport, AsyncClient
from PIL import Image

from app.main import app
from app.api.deps import get_current_user
from app.core.database import get_db
from app.models.scan import Scan
from app.models.user import User
from app.models.report import ScamReport
from app.services import scan_service, report_service
import app.core.database as database_core
import app.api.v1.scan as scan_api

BASELINE_ROOT = Path(os.environ.get("W06_BASELINE_ROOT", "/tmp/scamguard-w06-main"))
API_UPLOAD_DIR = Path(os.environ["LOCAL_UPLOAD_DIR"])


def make_image_bytes(fmt: str = "JPEG") -> bytes:
    image = Image.new("RGB", (32, 32), (255, 255, 255))
    buf = io.BytesIO()
    image.save(buf, format=fmt)
    return buf.getvalue()


class ScalarList:
    def __init__(self, first=None, all_items=None):
        self._first = first
        self._all = list(all_items or [])

    def first(self):
        return self._first

    def all(self):
        return self._all


class ExecResult:
    def __init__(self, *, first=None, all_items=None, scalar=None, scalar_one=None):
        self._scalars = ScalarList(first=first, all_items=all_items)
        self._scalar = scalar
        self._scalar_one = scalar_one

    def scalars(self):
        return self._scalars

    def scalar(self):
        return self._scalar

    def scalar_one_or_none(self):
        return self._scalar_one


class CreateDB:
    def __init__(self):
        self.added = []

    def add(self, obj):
        self.added.append(obj)

    async def commit(self):
        return None

    async def refresh(self, obj):
        if getattr(obj, "id", None) is None:
            obj.id = uuid.uuid4()
        if getattr(obj, "created_at", None) is None:
            obj.created_at = datetime.now(timezone.utc)


class GetScanDB:
    def __init__(self, scan):
        self.scan = scan

    async def execute(self, _stmt):
        return ExecResult(first=self.scan)


class ProcessDB:
    def __init__(self, scan):
        self.scan = scan
        self.commits = 0

    async def execute(self, _stmt):
        return ExecResult(first=self.scan)

    async def commit(self):
        self.commits += 1


class SessionFactory:
    def __init__(self, db):
        self.db = db

    def __call__(self):
        db = self.db

        class Ctx:
            async def __aenter__(self_inner):
                return db

            async def __aexit__(self_inner, *_exc):
                return False

        return Ctx()


class FakeRedis:
    def __init__(self, cached=None):
        self.cached = cached
        self.get_calls = []
        self.setex_calls = []

    async def get(self, key):
        self.get_calls.append(key)
        return json.dumps(self.cached) if self.cached is not None else None

    async def setex(self, key, ttl, value):
        self.setex_calls.append((key, ttl, json.loads(value)))
        return True


class HistoryDB:
    def __init__(self, scans):
        self.scans = scans
        self.calls = 0

    async def execute(self, _stmt):
        self.calls += 1
        if self.calls == 1:
            return ExecResult(scalar=len(self.scans))
        return ExecResult(all_items=self.scans)


class ReportDB:
    def __init__(self, scan, existing=None):
        self.scan = scan
        self.existing = existing
        self.calls = 0
        self.added = []

    async def execute(self, _stmt):
        self.calls += 1
        if self.calls == 1:
            return ExecResult(scalar_one=self.scan)
        return ExecResult(scalar_one=self.existing)

    def add(self, obj):
        self.added.append(obj)

    async def commit(self):
        return None

    async def refresh(self, obj):
        if getattr(obj, "id", None) is None:
            obj.id = 501
        if getattr(obj, "created_at", None) is None:
            obj.created_at = datetime.now(timezone.utc)


async def override_user_1():
    return User(id=1, email="w06@example.com", role="user")


@pytest.fixture(autouse=True)
def reset_app_state(monkeypatch):
    app.dependency_overrides.clear()
    app.dependency_overrides[get_current_user] = override_user_1
    stub_inference.calls = 0
    stub_inference.raise_exc = False
    stub_inference.result = {
        "visual_risk_score": 60,
        "ai_gen_probability": 0.60,
        "heatmap_bytes": b"",
        "ocr_text": "",
        "anomaly_region": "test region",
    }
    monkeypatch.setattr(report_service.manager, "broadcast", AsyncMock(return_value=None))
    yield
    app.dependency_overrides.clear()


async def api_request(method: str, path: str, **kwargs):
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        return await client.request(method, path, **kwargs)


def new_scan(*, user_id=1, status="completed", progress=100) -> Scan:
    scan = Scan(
        id=uuid.uuid4(),
        user_id=user_id,
        image_hash="a" * 64,
        raw_image_url="/tmp/w06-api-uploads/sample.png",
        heatmap_image_url=None,
        title="W06 fixture",
        text_score=10,
        visual_score=60,
        source_score=0,
        total_risk_score=60,
        ai_gen_probability=0.6,
        status=status,
        progress=progress,
        created_at=datetime.now(timezone.utc),
    )
    return scan


async def run_background(monkeypatch, tmp_path, *, cached=None, predict_result=None, raise_inference=False):
    scan = new_scan(status="uploading", progress=0)
    scan.raw_image_url = ""
    db = ProcessDB(scan)
    redis = FakeRedis(cached=cached)
    monkeypatch.setattr(database_core, "async_session", SessionFactory(db))
    monkeypatch.setattr(scan_service.redis_core, "redis_client", redis)
    monkeypatch.setattr(scan_service.settings, "LOCAL_UPLOAD_DIR", str(tmp_path))
    monkeypatch.setattr(scan_service.manager, "broadcast", AsyncMock(return_value=None))
    if predict_result is not None:
        stub_inference.result = dict(predict_result)
    stub_inference.raise_exc = raise_inference
    await scan_service.process_image_background(scan.id, make_image_bytes(), scan.image_hash)
    return scan, db, redis


@pytest.mark.asyncio
async def test_it01_upload_status_contract(monkeypatch):
    """FR-SCAN-02 AC-1 requires HTTP 202; baseline returns HTTP 200."""
    db = CreateDB()

    async def override_db():
        yield db

    async def no_background(*_args, **_kwargs):
        return None

    app.dependency_overrides[get_db] = override_db
    monkeypatch.setattr(scan_api, "process_image_background", no_background)
    files = {"file": ("w06.jpg", make_image_bytes(), "image/jpeg")}
    response = await api_request("POST", "/api/v1/scan/", files=files)
    assert response.status_code == 202, response.text
    assert response.json().get("id")


@pytest.mark.asyncio
async def test_it02_polling_contract():
    scan = new_scan(status="processing_visual", progress=50)
    db = GetScanDB(scan)

    async def override_db():
        yield db

    app.dependency_overrides[get_db] = override_db
    response = await api_request("GET", f"/api/v1/scan/{scan.id}")
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == str(scan.id)
    assert body["status"] == "processing_visual"
    assert body["progress"] == 50


@pytest.mark.asyncio
async def test_it03_cross_user_scan_is_forbidden():
    scan = new_scan(user_id=2)
    db = GetScanDB(scan)

    async def override_db():
        yield db

    app.dependency_overrides[get_db] = override_db
    response = await api_request("GET", f"/api/v1/scan/{scan.id}")
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_it04_mobile_cancel_contract_exists():
    scan_id = uuid.uuid4()
    response = await api_request("DELETE", f"/api/v1/scan/{scan_id}")
    assert response.status_code != 405, response.text


@pytest.mark.asyncio
async def test_it05_cache_hit_skips_inference(monkeypatch, tmp_path):
    cached = {
        "visual_risk_score": 70,
        "ai_gen_probability": 0.7,
        "ocr_text": "",
        "anomaly_region": "cached region",
    }
    scan, _db, redis = await run_background(monkeypatch, tmp_path, cached=cached)
    assert scan.status == "completed"
    assert stub_inference.calls == 0
    assert redis.get_calls
    assert redis.setex_calls == []


@pytest.mark.asyncio
async def test_it06_cache_miss_writes_30_day_ttl(monkeypatch, tmp_path):
    scan, _db, redis = await run_background(monkeypatch, tmp_path, cached=None)
    assert scan.status == "completed"
    assert stub_inference.calls == 1
    assert len(redis.setex_calls) == 1
    assert redis.setex_calls[0][1] == 2592000


@pytest.mark.asyncio
async def test_it07_cache_hit_requires_usable_heatmap_reference(monkeypatch, tmp_path):
    cached = {
        "visual_risk_score": 70,
        "ai_gen_probability": 0.7,
        "ocr_text": "",
        "anomaly_region": "cached region",
        "has_heatmap": True,
    }
    scan, _db, _redis = await run_background(monkeypatch, tmp_path, cached=cached)
    assert scan.status == "completed"
    assert scan.heatmap_image_url, "cache hit completed without the expected heatmap reference"


@pytest.mark.asyncio
async def test_it08_inference_output_maps_into_scan(monkeypatch, tmp_path):
    result = {
        "visual_risk_score": 80,
        "ai_gen_probability": 0.8,
        "heatmap_bytes": b"",
        "ocr_text": "ด่วน",
        "anomaly_region": "center",
    }
    scan, _db, _redis = await run_background(monkeypatch, tmp_path, predict_result=result)
    assert scan.status == "completed"
    assert scan.visual_score == 80
    assert scan.text_score == 25
    assert scan.ai_gen_probability == 0.8
    assert "ด่วน" in scan.scam_keywords_found


@pytest.mark.asyncio
async def test_it09_inference_failure_marks_scan_failed(monkeypatch, tmp_path):
    scan, _db, _redis = await run_background(monkeypatch, tmp_path, raise_inference=True)
    assert scan.status == "failed"
    assert scan.progress == 0


def test_it10_visual_dual_signal_contract_present():
    worker = (BASELINE_ROOT / "server/app/services/onnx_worker.py").read_text(encoding="utf-8")
    assert '"forgery_confidence"' in worker
    assert '"ai_gen_confidence"' in worker


@pytest.mark.asyncio
async def test_it12_source_api_down_excludes_source_dimension(monkeypatch, tmp_path):
    scan, _db, _redis = await run_background(monkeypatch, tmp_path)
    assert getattr(scan, "source_status", None) == "unavailable"
    assert scan.source_score == 0


@pytest.mark.asyncio
async def test_it13_heatmap_reference_is_canonical_upload_url(monkeypatch, tmp_path):
    result = {
        "visual_risk_score": 80,
        "ai_gen_probability": 0.8,
        "heatmap_bytes": b"fake-jpeg-bytes",
        "ocr_text": "",
        "anomaly_region": "center",
    }
    scan, _db, _redis = await run_background(monkeypatch, tmp_path, predict_result=result)
    assert scan.heatmap_image_url is not None
    assert scan.heatmap_image_url.startswith("/uploads/"), scan.heatmap_image_url


@pytest.mark.asyncio
async def test_it14_upload_mount_serves_media():
    media = API_UPLOAD_DIR / "heatmaps" / "w06.jpg"
    media.parent.mkdir(parents=True, exist_ok=True)
    media.write_bytes(b"w06-media")
    response = await api_request("GET", "/uploads/heatmaps/w06.jpg")
    assert response.status_code == 200
    assert response.content == b"w06-media"


@pytest.mark.asyncio
async def test_it15_history_lists_owned_completed_scan():
    scan = new_scan(status="completed", progress=100)
    db = HistoryDB([scan])

    async def override_db():
        yield db

    app.dependency_overrides[get_db] = override_db
    response = await api_request("GET", "/api/v1/history")
    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 1
    # Canonical FR-HISTORY-01 AC-1 names the collection `scans` and the grade field `risk_grade`.
    assert "scans" in body, body
    assert body["scans"][0]["scan_id"] == str(scan.id)
    assert body["scans"][0]["risk_score"] == scan.total_risk_score
    assert "risk_grade" in body["scans"][0]


def test_it16_history_supports_srs_filter_contract():
    import inspect
    from app.api.v1.history import get_history

    params = inspect.signature(get_history.__wrapped__ if hasattr(get_history, "__wrapped__") else get_history).parameters
    assert "start_date" in params
    assert "end_date" in params
    assert "risk_grade" in params


@pytest.mark.asyncio
async def test_it17_report_creation_persists_pending():
    scan = new_scan()
    db = ReportDB(scan)

    async def override_db():
        yield db

    app.dependency_overrides[get_db] = override_db
    payload = {
        "scan_id": str(scan.id),
        "category": "fake_slip",
        "description": "สลิปโอนเงินปลอม จำนวนเงินถูกแก้ไข",
    }
    response = await api_request("POST", "/api/v1/reports", json=payload)
    assert response.status_code == 201, response.text
    body = response.json()
    assert body["scan_id"] == str(scan.id)
    assert body["status"] == "pending"
    assert len(db.added) == 1
    # Canonical FR-HISTORY-02 AC-1 names the identifier `report_id`.
    assert body.get("report_id") is not None, body


@pytest.mark.asyncio
async def test_it18_duplicate_report_returns_409():
    scan = new_scan()
    existing = ScamReport(id=9, user_id=1, scan_id=scan.id, category="fake_slip", reason="already reported", status="pending")
    db = ReportDB(scan, existing=existing)

    async def override_db():
        yield db

    app.dependency_overrides[get_db] = override_db
    payload = {
        "scan_id": str(scan.id),
        "category": "fake_slip",
        "description": "สลิปโอนเงินปลอม จำนวนเงินถูกแก้ไข",
    }
    response = await api_request("POST", "/api/v1/reports", json=payload)
    assert response.status_code == 409
    assert db.added == []
    assert response.json().get("detail") == "You have already reported this scan"
