from logging import getLogger
from fastapi import FastAPI

from src.api.api import router
from src.core.config import APIConfigurations

logger = getLogger(__name__)

app = FastAPI(
    title=APIConfigurations.title,
    description=APIConfigurations.description,
    version=APIConfigurations.version
)

app.include_router(router, prefix=f"/{APIConfigurations.version}")
