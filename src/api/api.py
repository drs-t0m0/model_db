from fastapi import APIRouter

from src.api.routers import health, projects

router = APIRouter()

router.include_router(health.router, prefix="/health", tags=["health"])
router.include_router(projects.router, prefix="/projects", tags=["projects"])
