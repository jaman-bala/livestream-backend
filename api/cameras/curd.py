from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from db.models import Camera
from api.cameras.schemas import CameraBase
from db.session import get_db

async def create_camera(db: AsyncSession, camera: CameraBase):
    async with db.begin() as session:
        db_camera = Camera(**camera.dict())
        session.add(db_camera)
        await session.commit()
        await session.refresh(db_camera)
        return db_camera

async def get_cameras(db: AsyncSession):
    statement = select(Camera)
    result = await db.execute(statement)
    cameras = result.scalars().all()
    return cameras

async def get_camera_by_id(db: AsyncSession, camera_id: int):
    statement = select(Camera).filter(Camera.id == camera_id)
    result = await db.execute(statement)
    camera = result.scalars().first()
    return camera

async def update_camera(db: AsyncSession, camera_id: int, updated_camera: CameraBase):
    statement = select(Camera).filter(Camera.id == camera_id)
    result = await db.execute(statement)
    db_camera = result.scalars().first()

    if db_camera:
        for key, value in updated_camera.dict().items():
            setattr(db_camera, key, value)
        await db.commit()
        await db.refresh(db_camera)

    return db_camera

async def delete_camera(db: AsyncSession, camera_id: int):
    statement = select(Camera).filter(Camera.id == camera_id)
    result = await db.execute(statement)
    db_camera = result.scalars().first()

    if db_camera:
        db.delete(db_camera)
        await db.commit()

    return db_camera