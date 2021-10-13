from fastapi import APIRouter

from src.api.routers import health

router = APIRouter()

router.include_router(health.router, prefix="/health", tags=["health"])
