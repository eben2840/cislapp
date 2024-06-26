"""empty message

Revision ID: 9dafe38f3bb2
Revises: aeacb0c17497
Create Date: 2023-10-13 15:00:30.548764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dafe38f3bb2'
down_revision = 'aeacb0c17497'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pdf_file', schema=None) as batch_op:
        batch_op.add_column(sa.Column('year', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pdf_file', schema=None) as batch_op:
        batch_op.drop_column('year')

    # ### end Alembic commands ###
