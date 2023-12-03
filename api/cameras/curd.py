from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Camera
from api.cameras.schemas import CameraBase

async def create_camera(db: AsyncSession, camera: CameraBase):
    db_camera = Camera(**camera.dict())
    db.add(db_camera)
    await db.commit()
    await db.refresh(db_camera)
    return db_camera

async def get_cameras(db: AsyncSession):
    return await db.query(Camera).all()