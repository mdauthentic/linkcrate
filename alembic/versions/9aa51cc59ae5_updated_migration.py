"""updated migration

Revision ID: 9aa51cc59ae5
Revises: 170f199ce7c0
Create Date: 2024-09-08 11:55:50.941819

"""

from typing import Sequence, Union
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9aa51cc59ae5"
down_revision: Union[str, None] = "170f199ce7c0"
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
    op.drop_table("bookmark")
    # ### end Alembic commands ###
