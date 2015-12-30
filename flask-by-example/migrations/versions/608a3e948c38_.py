"""empty message

Revision ID: 608a3e948c38
Revises: None
Create Date: 2015-12-30 21:43:07.267116

"""

# revision identifiers, used by Alembic.
revision = '608a3e948c38'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('result_all', postgresql.JSON(), nullable=True),
    sa.Column('result_no_stop_words', postgresql.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results')
    ### end Alembic commands ###
