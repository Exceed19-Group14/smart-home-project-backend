from fastapi import APIRouter, status
from pydantic import BaseModel
from db.mongo import db
from enum import IntEnum
from typing import List


router = APIRouter(
    prefix='/room'
)


class ModeEnum(IntEnum):
    auto = 1
    manual = 0


class StateEnum(IntEnum):
    open = 1
    close = 0


class SetAutoModel(BaseModel):
    mode: ModeEnum


class SetState(BaseModel):
    state: StateEnum
    

class SetBrightnessLevel(BaseModel):
    brightness_level: int


class RoomModel(BaseModel):
    id: int
    state: StateEnum
    mode: ModeEnum
    brightness_level: SetBrightnessLevel


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=List[RoomModel])
def get_room(id: int):
    docs = list(db.get_collection('rooms').find({
        "id": id
    }, {"_id": False}))

    return docs


@router.put('/{id}/mode', status_code=status.HTTP_204_NO_CONTENT)
def set_mode(id: int, dto: SetAutoModel):
    db.get_collection('rooms').update_one({
        "id": id
    }, {
        "$set": {
            "mode": dto.mode
        }
    })


@router.put('/{id}/state', status_code=status.HTTP_204_NO_CONTENT)
def set_state(id: int, dto: SetState):
    db.get_collection('rooms').update_one({
        "id": id
    }, {
        "$set": {
            "state": dto.state
        }
    })


@router.put('/{id}/brightness', status_code=status.HTTP_204_NO_CONTENT)
def set_brightness(id: int, dto: SetBrightnessLevel):
    db.get_collection('rooms').update_one({
        "id": id
    }, {
        "$set": {
            "brightness": dto.brightness_level
        }
    })
