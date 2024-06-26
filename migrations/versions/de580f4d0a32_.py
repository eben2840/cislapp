"""empty message

Revision ID: de580f4d0a32
Revises: 918f68e68dd9
Create Date: 2024-03-10 14:08:13.327046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de580f4d0a32'
down_revision = '918f68e68dd9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.drop_column('telephone')
        batch_op.drop_column('contact')
        batch_op.drop_column('yearCompleted')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('yearCompleted', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('contact', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('telephone', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###
