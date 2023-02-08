from mongo import db
from routes.room import StateEnum, ModeEnum
db.get_collection("rooms").insert_many([{
    "id": i,
    "brightness_level": 127,
    "state": StateEnum.close,
    "mode": ModeEnum.manual
} for i in range(1, 4)])
