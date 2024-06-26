"""empty message

Revision ID: 918f68e68dd9
Revises: 580ba5756018
Create Date: 2024-03-10 12:23:52.649792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '918f68e68dd9'
down_revision = '580ba5756018'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company_email', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('company_name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('category', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.drop_column('category')
        batch_op.drop_column('company_name')
        batch_op.drop_column('company_email')

    # ### end Alembic commands ###
