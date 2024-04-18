"""empty message

Revision ID: a0dccab9f850
Revises: c7c6cb8a39b3
Create Date: 2024-04-17 15:04:48.903805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0dccab9f850'
down_revision = 'c7c6cb8a39b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hospital', schema=None) as batch_op:
        batch_op.drop_constraint('hospital_staff_id_fkey', type_='foreignkey')
        batch_op.drop_column('staff_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hospital', schema=None) as batch_op:
        batch_op.add_column(sa.Column('staff_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('hospital_staff_id_fkey', 'user', ['staff_id'], ['id'])

    # ### end Alembic commands ###