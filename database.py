from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///student.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = Session()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
