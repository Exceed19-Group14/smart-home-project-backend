from fastapi import APIRouter, status
from pydantic import BaseModel
from db.mongo import db
from enum import IntEnum
router = APIRouter(
    prefix='/room'
)


class ModeEnum(IntEnum):
    auto = 1
    manual = 0


class SetAutoModel(BaseModel):
    mode: ModeEnum


@router.put('/{id}/mode', status_code=status.HTTP_204_NO_CONTENT)
def setAuto(id: int, dto: SetAutoModel):
    db.get_collection('rooms').update_one({
        "id": id
    }, {
        "$set": {
            "mode": dto.mode
        }
    })
