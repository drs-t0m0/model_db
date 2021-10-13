from logging import getLogger
from fastapi import FastAPI

from src.api.api import router
from src.core.config import APIConfigurations
from src.db import initialize
from src.db.database import engine

logger = getLogger(__name__)

initialize.initialize_table(engine=engine, checkfirst=True)

app = FastAPI(
    title=APIConfigurations.title,
    description=APIConfigurations.description,
    version=APIConfigurations.version
)

app.include_router(router, prefix=f"/{APIConfigurations.version}")
