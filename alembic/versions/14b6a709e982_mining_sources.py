"""mining_sources

Revision ID: 14b6a709e982
Revises: 
Create Date: 2025-09-08 00:41:38.913972

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import datetime

from sqlalchemy import DateTime
from sqlalchemy import Date
from sqlalchemy.dialects.postgresql import JSON

# revision identifiers, used by Alembic.
revision: str = '14b6a709e982'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    create_table = op.create_table(
        'mining_sources', sa.Column('id', sa.Integer, primary_key=True),

        sa.Column('code', sa.Text(), nullable=True),
        sa.Column('name', sa.String(length=255), nullable=True),

        sa.Column('created_at', DateTime, nullable=True),
        sa.Column('updated_at', DateTime, nullable=True),
        sa.Column('deleted_at', DateTime, nullable=True),
    )


def downgrade() -> None:
    op.drop_table("mining_sources")
