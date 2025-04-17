from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///module10.db?check_same_thread=False'

Base = declarative_base()

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
