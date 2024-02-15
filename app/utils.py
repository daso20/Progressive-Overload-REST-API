from passlib.context import CryptContext
import os
import pandas as pd

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def read_from_xlsx(input_file):
    current_directory = os.path.dirname(os.path.abspath(__name__))
    exercises_file_path = os.path.join(current_directory, input_file)

    df = pd.read_excel(exercises_file_path)
    exercise_list = df.to_dict(orient='records')
    return exercise_list