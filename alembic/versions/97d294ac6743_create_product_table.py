"""create Product table

Revision ID: 97d294ac6743
Revises: 
Create Date: 2024-07-26 20:49:42.763082

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97d294ac6743'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'product',
    sa.Column('id', sa.Integer(), primary_key=True, nullable=False, autoincrement=True),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False)
    )

def downgrade() -> None:
    op.drop_table('product')
