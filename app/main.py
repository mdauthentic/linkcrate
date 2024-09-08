from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from alembic import command
from alembic.config import Config
from .routers import bookmark


alembic_config_path = Path(__file__).parent.parent / "alembic.ini"
alembic_cfg = Config(alembic_config_path)


@asynccontextmanager
async def on_startup(app: FastAPI):
    command.upgrade(alembic_cfg, "head")
    yield
    command.downgrade(alembic_cfg, "")


app = FastAPI(lifespan=on_startup)

app.include_router(bookmark.router)
