from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from db.session import get_db
from api.cameras.schemas import CameraOUT, CameraBase
from api.cameras.curd import get_cameras, get_camera_by_id, delete_camera, update_camera, create_camera

stream_router = APIRouter()

@stream_router.post("/cameras/", response_model=CameraOUT)
async def create_camera_handler(camera: CameraBase, db: AsyncSession = Depends(get_db)):
    return await create_camera(db=db, camera=camera)

@stream_router.get("/cameras/", response_model=List[CameraOUT])
async def read_cameras_handler(db: AsyncSession = Depends(get_db)):
    return await get_cameras(db=db)

@stream_router.get("/cameras/{camera_id}", response_model=CameraOUT)
async def read_camera_by_id_handler(camera_id: int, db: AsyncSession = Depends(get_db)):
    camera = await get_camera_by_id(db=db, camera_id=camera_id)
    if camera is None:
        raise HTTPException(status_code=404, detail="Camera not found")
    return camera

@stream_router.put("/cameras/{camera_id}", response_model=CameraOUT)
async def update_camera_handler(camera_id: int, updated_camera: CameraBase, db: AsyncSession = Depends(get_db)):
    camera = await update_camera(db=db, camera_id=camera_id, updated_camera=updated_camera)
    if camera is None:
        raise HTTPException(status_code=404, detail="Camera not found")
    return camera

@stream_router.delete("/cameras/{camera_id}", response_model=CameraOUT)
async def delete_camera_handler(camera_id: int, db: AsyncSession = Depends(get_db)):
    camera = await delete_camera(db=db, camera_id=camera_id)
    if camera is None:
        raise HTTPException(status_code=404, detail="Camera not found")
    return camera