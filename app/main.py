import logging
import sys
from typing import Annotated
from fastapi import Depends, FastAPI

from .utils.repositories import SQLAlchemyRepository
from .config import settings
from .routers import routers_list


logging.basicConfig(
    stream=sys.stdout, level=logging.DEBUG if settings.DEBUG else logging.INFO
)


app = FastAPI(title=settings.PROJECT_NAME)


for router in routers_list:
    app.include_router(router)
