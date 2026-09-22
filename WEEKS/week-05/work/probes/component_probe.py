#!/usr/bin/env python3
"""Week 05 reproducible component probes against an extracted ScamGuard server baseline."""
import asyncio
import inspect
import os
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("usage: component_probe.py <server-path>")
server_path = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(server_path))

# Safe test-only configuration. The probes never connect to these services.
os.environ.setdefault("ALLOWED_ORIGINS", "http://localhost")
os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://w05:w05@127.0.0.1:5432/w05")
os.environ.setdefault("JWT_SECRET_KEY", "week05-test-only-key")
os.environ.setdefault("REDIS_URL", "redis://127.0.0.1:6379/15")
os.environ.setdefault("ONNX_MODEL_PATH", "/tmp/week05-missing.onnx")
os.environ.setdefault("XAI_MODEL_PATH", "/tmp/week05-missing.gguf")

from app.utils.risk_calculator import calculate_risk_score
from app.api.v1 import auth

print("[RISK] canonical Hybrid max+bonus examples")
for values in [(50, 85, 0), (100, 100, 100), (10, 0, 0), (30, 0, 0), (55, 0, 0), (80, 0, 0), (0, 39, 0), (0, 40, 0), (0, 69, 0), (70, 0, 0)]:
    result = calculate_risk_score(*values)
    print(values, "->", result["total_risk_score"], result["grade"], result["primary_factor"], result["is_multi_risk"])

class FakeResult:
    def scalars(self):
        return self
    def first(self):
        return None

class FakeDb:
    def __init__(self):
        self.added = []
    async def execute(self, _statement):
        return FakeResult()
    def add(self, obj):
        self.added.append(obj)
    async def flush(self):
        for obj in self.added:
            if obj.__class__.__name__ == "User" and getattr(obj, "id", None) is None:
                obj.id = 1
    async def commit(self):
        return None
    async def refresh(self, _obj):
        return None

register_fn = auth.register
while hasattr(register_fn, "__wrapped__"):
    register_fn = register_fn.__wrapped__
auth.hash_password = lambda _pw: "mocked_hash"

async def probe_register(system_consent: bool, research_consent: bool):
    body = auth.RegisterRequest(
        email="week05@example.com",
        password="abcdefgh",
        full_name="Week05 Probe",
        system_consent=system_consent,
        research_consent=research_consent,
    )
    db = FakeDb()
    response = await register_fn(None, body, db)
    consent = next(obj for obj in db.added if obj.__class__.__name__ == "ConsentLog")
    return {
        "response_type": type(response).__name__,
        "response_keys": sorted(response.model_dump().keys()),
        "added_types": [obj.__class__.__name__ for obj in db.added],
        "consent": (consent.system_consent, consent.research_consent),
    }

print("[AUTH] register happy path")
print(asyncio.run(probe_register(True, False)))
print("[AUTH] system_consent=false behavior")
print(asyncio.run(probe_register(False, False)))

api_dir = server_path / "app" / "api" / "v1"
auth_text = (api_dir / "auth.py").read_text(encoding="utf-8")
users_text = (api_dir / "users.py").read_text(encoding="utf-8")
all_api_text = "\n".join(p.read_text(encoding="utf-8") for p in api_dir.glob("*.py"))
print("[CONSENT] route inventory")
print("PUT /consent/research present:", '"/consent/research"' in all_api_text)
print("GET /consent/logs present:", '"/consent/logs"' in all_api_text)
print("GET /auth/me present:", '@router.get("/me"' in auth_text)
print("users /me is DELETE:", '@router.delete("/me"' in users_text)

onnx_text = (server_path / "app" / "services" / "onnx_worker.py").read_text(encoding="utf-8")
print("[VISUAL] output-contract inventory")
print("max SegFormer probability assigned to ai_gen_prob:", "ai_gen_prob = float(prob_map_true.max())" in onnx_text)
print("same value converted to visual_risk_score:", "visual_risk_score = int(round(ai_gen_prob * 100))" in onnx_text)
print("separate forgery_confidence key present:", '"forgery_confidence"' in onnx_text)
print("separate ai_gen_confidence key present:", '"ai_gen_confidence"' in onnx_text)
