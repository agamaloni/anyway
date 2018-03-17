"""create user_locations table

Revision ID: 4510f6f63e5d
Revises: 3c0d35fdbe2e
Create Date: 2018-03-17 20:22:56.780000

"""

# revision identifiers, used by Alembic.
revision = '4510f6f63e5d'
down_revision = '3c0d35fdbe2e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

_table_name = "user_locations"

def downgrade():
    op.drop(_table_name)


def upgrade():
    op.create_table(
        _table_name,
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('email', sa.String(120), nullable=True),
        sa.Column('latitude', sa.Float(), nullable=True),
        sa.Column('longitude', sa.Float(), nullable=True),
        sa.Column('radius', sa.Float(), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
