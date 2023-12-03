from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
import cv2
import asyncio
from api.cameras.curd import get_cameras
from db.session import get_db

cv_router = APIRouter()

async def generate_frames(rtsp_url: str):
    cap = cv2.VideoCapture(rtsp_url)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@cv_router.get("/mjpeg/{camera_id}")
async def mjpeg_stream(
    camera_id: int,
    db: AsyncSession = Depends(get_db)
):
    camera = await get_cameras(db, camera_id)
    return StreamingResponse(
        generate_frames(camera.url),
        media_type="multipart/x-mixed-replace;boundary=frame"
    )