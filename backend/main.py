from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

PROJ_ROOT = Path(__file__).resolve().parent.parent
FRONTEND_DIST = PROJ_ROOT / "frontend" / "dist"
app.mount(
    "/",
    StaticFiles(directory=FRONTEND_DIST, html=True),
    name="frontend"
)

