from fastapi import FastAPI
from tasktracker.api.routes import router
from tasktracker.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

app.include_router(router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": "ok"}
