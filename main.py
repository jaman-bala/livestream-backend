import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter
from starlette_exporter import handle_metrics
from starlette_exporter import PrometheusMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from api.users.handlers import user_router
from api.users.login_handler import login_router
from api.service import service_router

from api.cameras.routes import stream_router
from api.opencv.cv import cv_router

#########################
# BLOCK WITH API ROUTES #
#########################

app = FastAPI()
origins = [
   "http://localhost:3000", # React app
]

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix="/api/user", tags=["user"])
main_api_router.include_router(login_router, prefix="/login", tags=["login"])
main_api_router.include_router(service_router, tags=["service"])
main_api_router.include_router(stream_router, tags=["/api/stream"])
app.include_router(cv_router, tags=["/api/mjpeg"])
app.include_router(main_api_router)

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
