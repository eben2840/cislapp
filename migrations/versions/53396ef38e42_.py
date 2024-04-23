"""empty message

Revision ID: 53396ef38e42
Revises: 062d7712afd3
Create Date: 2024-04-22 11:58:58.785942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53396ef38e42'
down_revision = '062d7712afd3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('clientname', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.drop_column('clientname')

    # ### end Alembic commands ###
