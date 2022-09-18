import sqlalchemy
from sqlalchemy import create_engine 


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlite3 import connect

SQLALCHEMY_DATABASE_URL = "sqlite:///fastdb.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = sqlalchemy.MetaData()
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
def conn():
    conn = connect('../fastdb.db')
    curs = conn.cursor()
    return curs