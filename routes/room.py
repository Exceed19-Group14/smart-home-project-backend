from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix='/room'
)


class SetAutoModel(BaseModel):
    mode: bool


@router.put('/{id}/auto')
def setAuto(id: int, dto: SetAutoModel):
    pass
