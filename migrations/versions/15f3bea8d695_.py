"""empty message

Revision ID: 15f3bea8d695
Revises: 780f8d8918d0
Create Date: 2024-04-16 20:06:55.047601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15f3bea8d695'
down_revision = '780f8d8918d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cisl', schema=None) as batch_op:
        batch_op.add_column(sa.Column('clientid', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cisl', schema=None) as batch_op:
        batch_op.drop_column('clientid')

    # ### end Alembic commands ###