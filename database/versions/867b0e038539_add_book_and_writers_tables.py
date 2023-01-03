"""add_book_and_writers_tables

Revision ID: 867b0e038539
Revises: 
Create Date: 2023-01-03 14:28:41.585719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '867b0e038539'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('writers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('lastname', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('writer', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('publish_date', sa.DateTime(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('cover_filename', sa.String(length=1000), nullable=False),
    sa.Column('genres', sa.String(length=1000), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['writer'], ['writers.id'], name='fk_books_writers_id_writer'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_table('writers')
    # ### end Alembic commands ###