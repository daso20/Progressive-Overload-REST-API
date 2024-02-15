from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/exercise",
    tags=["Exercise"]
)

@router.get('/')
def get_excercises(db : Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    exercises = db.query(models.Exercise).all()
    return {"data": exercises}

@router.get('/muscle/{muscle}')
def get_excercises_by_prim_muscle(muscle: str, db : Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    ret_muscle = db.query(models.Exercise).filter(models.Exercise.prim_muscle == muscle).all()
    if not ret_muscle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Primary muscle \'{muscle}\' not found on database")

    return {"data": ret_muscle}

@router.get('/equipment/{equipment}')
def get_excercises_by_equipment(equipment:str, db : Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    ret_equipment= db.query(models.Exercise).filter(models.Exercise.used_equipment == equipment).all()
    if not ret_equipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Equipment \'{equipment}\' not found on database")

    return {"data": ret_equipment}

@router.get('/fetch_exercise/{equipment}/{muscle}')
def get_excercises_by_equipment(equipment:str, muscle:str, db : Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    ret_equipment= db.query(models.Exercise).filter(models.Exercise.used_equipment == equipment, models.Exercise.prim_muscle == muscle).first()
    if not ret_equipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Equipment \'{equipment}\' or primary muscle \'{muscle}\' not found on database")
    
    return {"data": ret_equipment}