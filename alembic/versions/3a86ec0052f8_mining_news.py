"""mining_news

Revision ID: 3a86ec0052f8
Revises: bddaaeb9e2e6
Create Date: 2025-09-08 00:53:08.385872

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import datetime

from sqlalchemy import DateTime
from sqlalchemy import Date
from sqlalchemy.dialects.postgresql import JSON

# revision identifiers, used by Alembic.
revision: str = '3a86ec0052f8'
down_revision: Union[str, Sequence[str], None] = 'bddaaeb9e2e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    create_table = op.create_table(
        'mining_news', sa.Column('id', sa.Integer, primary_key=True),

        sa.Column('mining_source_id', sa.Integer, nullable=True),

        sa.Column('code', sa.Text(), nullable=True),
        sa.Column('data', JSON, nullable=True),

        sa.Column('title', sa.Text(), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('published_date', sa.String(length=255), nullable=True),
        sa.Column('url', sa.Text(), nullable=True),

        sa.Column('publisher_href', sa.Text(), nullable=True),
        sa.Column('publisher_title', sa.String(length=255), nullable=True),

        sa.Column('status_validation', sa.String(length=255), nullable=True),

        sa.Column('created_at', DateTime, nullable=True),
        sa.Column('updated_at', DateTime, nullable=True),
        sa.Column('deleted_at', DateTime, nullable=True),
    )


def downgrade() -> None:
    op.drop_table("mining_news")
