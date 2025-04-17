from datetime import datetime
from pydantic import BaseModel, Field

from typing import Optional

class User(BaseModel):
    name: str
    surname: str

class UserGet(BaseModel):
    first_name: str
    surname: str
    recommended_by: Optional['UserGet'] = None

    class Config:
        orm_mode = True


class FacilityGet(BaseModel):
    name: str
    membercost: int
    guestcost: int
    initialoutlay: int
    monthlymaintenance: int

    class Config:
        orm_mode = True

class BookingGet(BaseModel):
    member_id: int
    member_rl: UserGet
    facility_id: int
    facility_rl: Optional['FacilityGet']
    start_time: datetime
    slots: int

    class Config:
        orm_mode = True