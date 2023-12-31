"""Adding Trip  model

Revision ID: 25a3d369232b
Revises: d0a0b2f013d0
Create Date: 2023-08-22 10:18:35.185341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25a3d369232b'
down_revision: Union[str, None] = 'd0a0b2f013d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trips',
    sa.Column('trip_id', sa.Integer(), nullable=False),
    sa.Column('start_place', sa.String(), nullable=True),
    sa.Column('end_place', sa.String(), nullable=True),
    sa.Column('avg_gas_price', sa.Float(), nullable=True),
    sa.Column('fuel_efficiency_mpg', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name=op.f('fk_trips_user_id_users')),
    sa.PrimaryKeyConstraint('trip_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trips')
    # ### end Alembic commands ###
