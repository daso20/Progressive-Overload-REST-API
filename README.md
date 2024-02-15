REST-API Endpoint to fetch data from PostgreSQL database. Developed in Python version 3.11.4. File "requirements.txt" available with Python modules used to run the project.

Requires the following additional files in top directory:
- "exercises.xlsx" (saved as "Excel Workbook", not as "Strict Open XML Spreadsheet") which will contain the exercises added to the database. Example data would look as the following:

| id | exercise_name | used_equipment	| prim_muscle | sec_muscles |
--- | --- | --- | --- | --- 
| 1	| Bench Press	| Barbell	|  Pectoralis Major (Sternal)	| Pectoralis Major (Clavicular), Deltoid, Triceps |
--- | --- | --- | --- | --- 
| 2	| Lever Incline Row |	Lerver	| Back | Trapezius, Latissimus |                           |

 
- ".env" file for private data. Contains the following parameters:
DATABASE_HOSTNAME
DATABASE_PORT
DATABASE_NAME
DATABASE_USERNAME
DATABASE_PASSWORD
SECRET_KEY
ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES
CLEAR_PASSWORD

Commands to run the application:
1.- Generate database data:
# alembic upgrade head 
2.- Run FASTAPI application:
# uvicorn app.main:app --reload --host <IP_address> --port <Port>

Documentation on endpoints can be found under http://<IP_address>:<Port>/docs after starting the uvicorn service.
