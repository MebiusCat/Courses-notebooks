import os
import psycopg2

from dotenv import load_dotenv
from typing import List
import uvicorn

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .schema_db import SessionLocal, Booking, Facility, Member
from .models import BookingGet, UserGet, FacilityGet


app = FastAPI()


def get_db_postgresql():
    with psycopg2.connect(
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        host=os.environ['POSTGRES_HOST'],
        port=os.environ['POSTGRES_PORT'],
        database=os.environ['POSTGRES_DATABASE']
    ) as conn:
        return conn

def get_db():
    with SessionLocal() as db:
        return db


@app.get('/user/all', response_model=List[UserGet])
def show_users(limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Member).limit(limit).all()


@app.get('/bookings/show', response_model=List[BookingGet])
def show_bookings(limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Booking).limit(limit).all()


@app.get('/facilities', response_model=List[FacilityGet])
def show_bookings(limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Facility).limit(limit).all()


@app.get('/bookings/hacks')
def show_bookings(limit: int = 10, db: Session = Depends(get_db)):
    for el in db.query(Booking).limit(limit).all():
        print(f'{el.member_rl.surname}')


if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app)