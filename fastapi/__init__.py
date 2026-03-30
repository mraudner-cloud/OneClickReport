"""A lightweight subset implementation of FastAPI used for local testing."""
from __future__ import annotations

from typing import Any, Callable, Dict, Tuple


class FastAPI:
    """Minimal FastAPI-compatible interface for defining request handlers."""

    def __init__(self) -> None:
        self._routes: Dict[Tuple[str, str], Callable[[], Any]] = {}

    def get(self, path: str) -> Callable[[Callable[[], Any]], Callable[[], Any]]:
        """Register a handler for HTTP GET requests."""

        def decorator(func: Callable[[], Any]) -> Callable[[], Any]:
            self._routes[("GET", path)] = func
            return func

        return decorator

    def dispatch(self, method: str, path: str) -> Any:
        """Execute the handler associated with a request."""
        try:
            handler = self._routes[(method, path)]
        except KeyError as exc:
            raise ValueError(f"No handler registered for {method} {path}") from exc
        return handler()


__all__ = ["FastAPI"]
