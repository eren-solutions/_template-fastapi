"""{{PROJECT_NAME}} — FastAPI Application."""

from fastapi import FastAPI

app = FastAPI(
    title="{{PROJECT_NAME}}",
    version="0.1.0",
    description="{{PROJECT_DESCRIPTION}}",
)


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to {{PROJECT_NAME}}"}
