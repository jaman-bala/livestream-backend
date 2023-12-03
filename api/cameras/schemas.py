from pydantic import BaseModel


class TunedModel(BaseModel):
    class Config:
        orm_mode = True


class CameraBase(TunedModel):
    title: str
    url: str


class CameraOUT(CameraBase):
    id: int
