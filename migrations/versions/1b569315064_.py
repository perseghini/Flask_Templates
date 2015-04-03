"""empty message

Revision ID: 1b569315064
Revises: 16656c9be87
Create Date: 2015-04-03 11:14:57.583594

"""

# revision identifiers, used by Alembic.
revision = '1b569315064'
down_revision = '16656c9be87'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('hash_password', sa.String(length=66), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###
