"""empty message

Revision ID: 30cd5a690675
Revises: 411874999d3a
Create Date: 2024-04-08 01:55:36.917287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30cd5a690675'
down_revision = '411874999d3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('code', sa.String(), nullable=True))
        batch_op.drop_column('username')
        batch_op.drop_column('category')
        batch_op.drop_column('company_email')
        batch_op.drop_column('company_name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company_name', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('company_email', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('category', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('username', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('code')

    # ### end Alembic commands ###