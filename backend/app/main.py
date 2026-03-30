"""FastAPI application entrypoint."""
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check() -> dict[str, str]:
    """Return service health information."""
    return {"status": "ok"}
