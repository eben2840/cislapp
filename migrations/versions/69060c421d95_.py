"""empty message

Revision ID: 69060c421d95
Revises: a088d8561dae
Create Date: 2024-04-22 11:14:24.451098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69060c421d95'
down_revision = 'a088d8561dae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cisl', schema=None) as batch_op:
        batch_op.alter_column('clientid',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=True)
        batch_op.drop_column('unique_code')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cisl', schema=None) as batch_op:
        batch_op.add_column(sa.Column('unique_code', sa.VARCHAR(length=12), autoincrement=False, nullable=True))
        batch_op.alter_column('clientid',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    # ### end Alembic commands ###
