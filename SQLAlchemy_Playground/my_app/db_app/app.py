import os
import psycopg2
import yaml

from dotenv import load_dotenv
from typing import List
import uvicorn

from fastapi import Depends, FastAPI
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection, cursor
from sqlalchemy.orm import Session

from .schema_db import SessionLocal, Booking, Facility, Member
from .models import BookingGet, UserGet, FacilityGet


app = FastAPI()


def config():
    with open("params.yaml") as f:
        return yaml.safe_load(f)


def get_db_postgresql() -> cursor:
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


@app.get('/user')
def get_user(limit, db: connection = Depends(get_db_postgresql), config: dict = Depends(config)):
    with db.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(
            """
            SELECT *
            FROM "user"
            LIMIT %(limit_user)s
            WHERE date >= %(start_date)s
            """,
            {'limit_user': limit, "start_date": config["feed_start_date"]})
        return cursor.fetchall()


if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app)