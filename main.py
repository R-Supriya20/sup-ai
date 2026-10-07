from fastapi import FastAPI

from config.settings import settings
from routers.health import router as health_router

from middleware.request_id import RequestIDMiddleware

from exceptions.handlers import (AppException,app_exception_handler)

from routers.auth import router as auth_router
from routers.admin import router as admin_router

from app_logging.logger import setup_logging


logger = setup_logging()


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)


# Middleware
app.add_middleware(
    RequestIDMiddleware
)


# Exception handlers
app.add_exception_handler(
    AppException,
    app_exception_handler
)


# Routers
app.include_router(
    health_router
)

app.include_router(
    auth_router
)

app.include_router(
    admin_router
)

@app.get("/")
def root():

    return {
        "message": "AI Customer Support Backend is running"
    }