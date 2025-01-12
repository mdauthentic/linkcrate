"""Initial migration

Revision ID: 170f199ce7c0
Revises: 
Create Date: 2024-09-08 11:45:43.022078

"""

from typing import Sequence, Union
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "170f199ce7c0"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "bookmark",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=True, index=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("url", sa.String(), unique=True, nullable=False, index=True),
        sa.Column(
            "date_created", sa.DateTime(), nullable=False, default=datetime.now()
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
