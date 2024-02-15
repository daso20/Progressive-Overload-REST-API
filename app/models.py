from sqlalchemy import Column, Integer, String

from .database import Base

class Exercise(Base):
    __tablename__ = "exercises"
    
    id = Column(Integer, primary_key=True, nullable=False)
    exercise_name = Column(String, nullable=False)
    used_equipment = Column(String, nullable=False)
    prim_muscle = Column(String, nullable=False)
    sec_muscles = Column(String, nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)