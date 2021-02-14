"""fix and add Follow

Revision ID: 11d5e3302eb2
Revises: 7b8b8f62d407
Create Date: 2020-12-16 12:12:51.766524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11d5e3302eb2'
down_revision = '7b8b8f62d407'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    op.drop_column('posts', 'body_html')
    op.drop_column('posts', 'title')
    op.drop_column('posts', 'title_html')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('title_html', sa.TEXT(), nullable=True))
    op.add_column('posts', sa.Column('title', sa.TEXT(), nullable=True))
    op.add_column('posts', sa.Column('body_html', sa.TEXT(), nullable=True))
    op.drop_table('follows')
    # ### end Alembic commands ###
