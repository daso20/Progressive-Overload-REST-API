"""create database tables

Revision ID: 14dc11c89dd2
Revises: 
Create Date: 2024-02-14 14:59:01.169469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app import utils, config
clear_text_password = config.settings.clear_password
hashed_pasword = utils.hash(clear_text_password)

exercises_list = utils.read_from_xlsx("exercises.xlsx")

# revision identifiers, used by Alembic.
revision: str = '14dc11c89dd2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    exercises_table = op.create_table('exercises',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('exercise_name', sa.String(), nullable=False),
                    sa.Column('used_equipment', sa.String(), nullable=False),
                    sa.Column('prim_muscle', sa.String(), nullable=False),
                    sa.Column('sec_muscles', sa.String(), nullable=False))
    users_table = op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False))
    op.bulk_insert(exercises_table, exercises_list)
    op.bulk_insert(users_table, 
    [
        {
            "id": 1,
            "email": "admin@global.com",
            "password": f"{hashed_pasword}"
        }
    ]               
    )


def downgrade():
    op.drop_table('exercises')
    op.drop_table('users')