from fastapi import FastAPI

from app.routes.users import users_router

app: FastAPI = FastAPI()

app.include_router(users_router, prefix="/api/users")

