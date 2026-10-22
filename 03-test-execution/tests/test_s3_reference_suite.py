#!/usr/bin/env python3
"""S3-B1 reference-suite probe for FR-AUTH-01 / FR-PDPA-01.

Runs the ten reference TCs from ENGSE601 worksheet 2 part B against the
ScamGuard FastAPI app at the pinned local commit, using an in-process
ASGI transport and an isolated in-memory session double.

Usage (from the project server directory, using its venv):
    ./venv/bin/python path/to/test_s3_reference_suite.py
Set SCAMGUARD_SERVER if the server directory is not /home/panuwat/project/server.
This is a standalone probe, not a pytest module.
"""
import asyncio
import os
import re
import sys
from pathlib import Path

SERVER = Path(os.environ.get("SCAMGUARD_SERVER", "/home/panuwat/project/server")).resolve()
sys.path.insert(0, str(SERVER))

os.environ.setdefault("ALLOWED_ORIGINS", "http://localhost")
os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://probe:probe@127.0.0.1:5432/probe")
os.environ.setdefault("JWT_SECRET_KEY", "s3-probe-test-only-key")
os.environ.setdefault("REDIS_URL", "redis://127.0.0.1:6379/15")
os.environ.setdefault("ONNX_MODEL_PATH", "/tmp/s3-missing.onnx")
os.environ.setdefault("XAI_MODEL_PATH", "/tmp/s3-missing.gguf")
os.environ.setdefault("RATE_LIMIT_GUEST_PER_MINUTE", "1000")
os.environ.setdefault("RATE_LIMIT_USER_PER_MINUTE", "1000")

from httpx import ASGITransport, AsyncClient
from app.main import app
from app.core.database import get_db
from app.models.user import User
from app.models.consent import ConsentLog

class Store:
    def __init__(self):
        self.users = []
        self.consents = []
        self.next_user_id = 1

STORE = Store()

class FakeScalars:
    def __init__(self, rows): self.rows = rows
    def first(self): return self.rows[0] if self.rows else None
    def all(self): return self.rows

class FakeResult:
    def __init__(self, rows): self.rows = rows
    def scalars(self): return FakeScalars(self.rows)

class FakeSession:
    def __init__(self, store): self.store = store
    async def execute(self, statement):
        sql = str(statement.compile(compile_kwargs={"literal_binds": True}))
        email = re.search(r"users\.email = '([^']*)'", sql)
        if email:
            return FakeResult([u for u in self.store.users if u.email == email.group(1)])
        uid = re.search(r"users\.id = (\d+)", sql)
        if uid:
            return FakeResult([u for u in self.store.users if u.id == int(uid.group(1))])
        return FakeResult([])
    def add(self, obj):
        if isinstance(obj, User):
            if obj.id is None:
                obj.id = self.store.next_user_id
                self.store.next_user_id += 1
            if obj.is_active is None:
                obj.is_active = True
            self.store.users.append(obj)
        elif isinstance(obj, ConsentLog):
            self.store.consents.append(obj)
    async def flush(self): return None
    async def commit(self): return None
    async def refresh(self, _obj): return None

async def override_get_db():
    yield FakeSession(STORE)

app.dependency_overrides[get_db] = override_get_db

def reset_store():
    global STORE
    STORE = Store()

def make_user(email, password_hash="existing_hash"):
    u = User(id=STORE.next_user_id, email=email, hashed_password=password_hash,
             full_name="Existing User", role="user", is_active=True)
    STORE.next_user_id += 1
    STORE.users.append(u)
    STORE.consents.append(ConsentLog(user_id=u.id, system_consent=True, research_consent=False))
    return u

def snapshot():
    return len(STORE.users), len(STORE.consents)

def check(cond, detail):
    return "Pass" if cond else "Fail", detail

async def main():
    results = []
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://probe") as client:
        # TC-01 password 7
        reset_store(); u0, c0 = snapshot()
        r = await client.post("/api/v1/auth/register", json={
            "email": "new.user09@example.com", "password": "Test123",
            "full_name": "Probe 01", "system_consent": True, "research_consent": False})
        u1, c1 = snapshot()
        ok = (r.status_code == 400 and "Password must be at least 8 characters" in r.text
              and (u1, c1) == (u0, c0))
        results.append(("TC-01", *check(ok, f"HTTP {r.status_code} · body={r.text[:160]} · users {u0}->{u1} · consents {c0}->{c1}")))

        # TC-02 password 8
        reset_store()
        r = await client.post("/api/v1/auth/register", json={
            "email": "new.user02@example.com", "password": "Test1234",
            "full_name": "Probe 02", "system_consent": True, "research_consent": False})
        created = STORE.users[0] if STORE.users else None
        consent = STORE.consents[0] if STORE.consents else None
        ok = (r.status_code == 201 and created is not None and len(STORE.users) == 1
              and consent is not None and consent.system_consent is True
              and created.hashed_password not in ("Test1234", None))
        results.append(("TC-02", *check(ok, f"HTTP {r.status_code} · users={len(STORE.users)} · consents={len(STORE.consents)} · hashed={str(getattr(created,'hashed_password',''))[:18]}… · system={getattr(consent,'system_consent',None)}")))

        # TC-03 empty password
        reset_store(); u0, c0 = snapshot()
        r = await client.post("/api/v1/auth/register", json={
            "email": "new.user07@example.com", "password": "",
            "full_name": "Probe 03", "system_consent": True, "research_consent": False})
        u1, c1 = snapshot()
        ok = (r.status_code == 400 and "Password must be at least 8 characters" in r.text
              and (u1, c1) == (u0, c0))
        results.append(("TC-03", *check(ok, f"HTTP {r.status_code} · body={r.text[:160]} · users {u0}->{u1} · consents {c0}->{c1}")))

        # TC-04 duplicate email
        reset_store(); make_user("test.user01@example.com"); u0, c0 = snapshot()
        r = await client.post("/api/v1/auth/register", json={
            "email": "test.user01@example.com", "password": "Test1234",
            "full_name": "Probe 04", "system_consent": True, "research_consent": False})
        u1, c1 = snapshot()
        ok = (r.status_code == 400 and "Email already registered" in r.text and (u1, c1) == (u0, c0))
        results.append(("TC-04", *check(ok, f"HTTP {r.status_code} · body={r.text[:160]} · users {u0}->{u1} · consents {c0}->{c1}")))

        # TC-05 withdraw research consent
        reset_store(); u0, c0 = snapshot()
        reg5 = await client.post("/api/v1/auth/register", json={
            "email": "withdraw.user@example.com", "password": "Test1234",
            "full_name": "Probe 05", "system_consent": True, "research_consent": True})
        login5 = await client.post("/api/v1/auth/login",
            data={"username": "withdraw.user@example.com", "password": "Test1234"},
            headers={"Content-Type": "application/x-www-form-urlencoded"})
        token5 = login5.json().get("access_token") if login5.status_code == 200 else None
        put5 = await client.put("/api/v1/consent/research", json={"is_granted": False},
            headers={"Authorization": f"Bearer {token5}"} if token5 else {})
        logs5 = await client.get("/api/v1/consent/logs",
            headers={"Authorization": f"Bearer {token5}"} if token5 else {})
        u1, c1 = snapshot()
        put_body = put5.text.replace(" ", "")[:200]
        logs_body = logs5.text.replace(" ", "")[:160]
        ok = (reg5.status_code == 201 and login5.status_code == 200
              and put5.status_code == 200 and '"consent_type":"research"' in put_body
              and '"is_granted":false' in put_body and '"updated_at"' in put_body
              and logs5.status_code == 200 and '"is_granted":false' in logs_body)
        results.append(("TC-05", *check(ok, f"register HTTP {reg5.status_code} · login HTTP {login5.status_code} · PUT /consent/research HTTP {put5.status_code} · body={put5.text[:160]} · GET /consent/logs HTTP {logs5.status_code} · body={logs5.text[:120]} · users {u0}->{u1} · consents {c0}->{c1}")))

        # TC-06 system consent false
        reset_store(); u0, c0 = snapshot()
        r = await client.post("/api/v1/auth/register", json={
            "email": "new.user04@example.com", "password": "Test1234",
            "full_name": "Probe 06", "system_consent": False, "research_consent": False})
        u1, c1 = snapshot()
        ok = (r.status_code == 400 and "System consent is required" in r.text and (u1, c1) == (u0, c0))
        results.append(("TC-06", *check(ok, f"HTTP {r.status_code} · body={r.text[:160]} · users {u0}->{u1} · consents {c0}->{c1}")))

        # TC-07 missing system consent field
        reset_store(); u0, c0 = snapshot()
        r = await client.post("/api/v1/auth/register", json={
            "email": "new.user08@example.com", "password": "Test1234",
            "full_name": "Probe 07", "research_consent": False})
        u1, c1 = snapshot()
        ok = (r.status_code == 400 and "System consent is required" in r.text
              and (u1, c1) == (u0, c0))
        results.append(("TC-07", *check(ok, f"HTTP {r.status_code} · body={r.text[:160]} · users {u0}->{u1} · consents {c0}->{c1}")))

        # TC-08 research consent false
        reset_store()
        r = await client.post("/api/v1/auth/register", json={
            "email": "new.user05@example.com", "password": "Test1234",
            "full_name": "Probe 08", "system_consent": True, "research_consent": False})
        consent = STORE.consents[0] if STORE.consents else None
        ok = (r.status_code == 201 and consent is not None and consent.research_consent is False)
        results.append(("TC-08", *check(ok, f"HTTP {r.status_code} · research={getattr(consent,'research_consent',None)}")))

        # TC-09 research consent true
        reset_store()
        r = await client.post("/api/v1/auth/register", json={
            "email": "new.user06@example.com", "password": "Test1234",
            "full_name": "Probe 09", "system_consent": True, "research_consent": True})
        consent = STORE.consents[0] if STORE.consents else None
        ok = (r.status_code == 201 and consent is not None and consent.research_consent is True)
        results.append(("TC-09", *check(ok, f"HTTP {r.status_code} · research={getattr(consent,'research_consent',None)}")))

        # TC-10 consent history
        reset_store()
        reg10 = await client.post("/api/v1/auth/register", json={
            "email": "history.user@example.com", "password": "Test1234",
            "full_name": "Probe 10", "system_consent": True, "research_consent": True})
        login = await client.post("/api/v1/auth/login",
            data={"username": "history.user@example.com", "password": "Test1234"},
            headers={"Content-Type": "application/x-www-form-urlencoded"})
        token = login.json().get("access_token") if login.status_code == 200 else None
        r = await client.get("/api/v1/consent/logs", headers={"Authorization": f"Bearer {token}"} if token else {})
        ok = (r.status_code == 200 and "logs" in r.text)
        results.append(("TC-10", *check(ok, f"register HTTP {reg10.status_code} · login HTTP {login.status_code} · GET /consent/logs HTTP {r.status_code} · body={r.text[:120]}")))

    print("S3-B1 API reference suite · ScamGuard · FR-AUTH-01 / FR-PDPA-01")
    repo = SERVER.parent
    commit = os.popen(f"git -C {repo} rev-parse --short HEAD").read().strip()
    print(f"Baseline: {SERVER} · commit", commit)
    print("Transport: httpx ASGITransport (in-process), isolated in-memory session")
    print("-" * 100)
    passed = failed = 0
    for tc, status, detail in results:
        print(f"{tc}  {status:4s}  {detail}")
        passed += status == "Pass"; failed += status == "Fail"
    print("-" * 100)
    print(f"Summary: {passed} Pass, {failed} Fail, {len(results)} total")

if __name__ == "__main__":
    asyncio.run(main())
