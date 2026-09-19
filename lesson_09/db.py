from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String


DATABASE_URL = (
    "postgresql://postgres:12345@localhost:5432/school"
)

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    user_id = Column(Integer, primary_key=True)
    level = Column(String)
    education_form = Column(String)
    subject_id = Column(Integer)