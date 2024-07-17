from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.v1.api import router

# origins = ["http://localhost.tiangolo.com","https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080", "http://localhost:5173/", "http://localhost:8000",
#     "http://ec2-3-16-115-196.us-east-2.compute.amazonaws.com:8000"]

def get_application():
    _app = FastAPI(title="OGSS FastAPI")

    _app.add_middleware(
        CORSMiddleware,
        # allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    _app.include_router(router)

    @_app.get('/')
    def home():
        return {"Message": "Home page"}

    return _app


app = get_application()
