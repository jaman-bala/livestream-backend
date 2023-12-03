from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from db.session import get_db
from api.cameras.schemas import CameraOUT
from api.cameras.schemas import CameraBase
from api.cameras.curd import create_camera, get_cameras

stream_router = APIRouter()

@stream_router.post("/cameras/", response_model=CameraOUT)
async def create_camera_handler(camera: CameraBase, db: AsyncSession = Depends(get_db)):
    return await create_camera(db=db, camera=camera)

@stream_router.get("/cameras/", response_model=List[CameraOUT])
async def read_cameras_handler(db: AsyncSession = Depends(get_db)):
    return await get_cameras(db=db)