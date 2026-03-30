"""Minimal test client compatible with the stub FastAPI implementation."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from . import FastAPI


@dataclass
class _Response:
    status_code: int
    data: Any

    def json(self) -> Any:
        return self.data


class TestClient:
    """Simple test client that executes handlers directly."""

    def __init__(self, app: FastAPI) -> None:
        self._app = app

    def get(self, path: str) -> _Response:
        body = self._app.dispatch("GET", path)
        return _Response(status_code=200, data=body)


__all__ = ["TestClient"]
