from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.users import users_router

app: FastAPI = FastAPI()

origins: list[str] = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(users_router, prefix="/api/users")

