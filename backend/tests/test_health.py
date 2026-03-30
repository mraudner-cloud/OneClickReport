"""Smoke test for the health endpoint."""
from __future__ import annotations

import sys
from pathlib import Path

# Ensure the repository root (which contains the FastAPI stub) is importable.
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from fastapi.testclient import TestClient

from app.main import app


def test_health_endpoint_returns_ok_status() -> None:
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
