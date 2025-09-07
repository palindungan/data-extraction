"""mining_news_histories

Revision ID: bddaaeb9e2e6
Revises: 14b6a709e982
Create Date: 2025-09-08 00:45:12.392388

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import datetime

from sqlalchemy import DateTime
from sqlalchemy import Date
from sqlalchemy.dialects.postgresql import JSON

# revision identifiers, used by Alembic.
revision: str = 'bddaaeb9e2e6'
down_revision: Union[str, Sequence[str], None] = '14b6a709e982'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    create_table = op.create_table(
        'mining_news_histories', sa.Column('id', sa.Integer, primary_key=True),

        sa.Column('mining_source_id', sa.Integer, nullable=True),

        sa.Column('code', sa.Text(), nullable=True),
        sa.Column('data', JSON, nullable=True),

        sa.Column('created_at', DateTime, nullable=True),
        sa.Column('updated_at', DateTime, nullable=True),
        sa.Column('deleted_at', DateTime, nullable=True),
    )


def downgrade() -> None:
    op.drop_table("mining_news_histories")
