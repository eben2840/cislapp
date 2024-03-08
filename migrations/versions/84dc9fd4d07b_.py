"""empty message

Revision ID: 84dc9fd4d07b
Revises: d7f6a2d2d76a
Create Date: 2024-02-11 13:41:50.138592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84dc9fd4d07b'
down_revision = 'd7f6a2d2d76a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('group_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'groups', ['group_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('group_id')

    # ### end Alembic commands ###