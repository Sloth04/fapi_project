"""add_books_table

Revision ID: 6496999bd191
Revises: 0c6fd55cc976
Create Date: 2023-01-03 12:05:05.286051

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6496999bd191'
down_revision = '0c6fd55cc976'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "books",
        sa.Column("id", mysql.BIGINT(unsigned=True), autoincrement=True, nullable=False),
        sa.Column("title", mysql.VARCHAR(255), nullable=False),
        sa.Column("writer", mysql.VARCHAR(255), nullable=False),
        sa.Column("description", mysql.TEXT(), nullable=True),
        sa.Column("publish_date", mysql.TIMESTAMP(), nullable=False, server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("rating", mysql.TINYINT(), nullable=True),
        sa.Column("cover_filename", mysql.VARCHAR(255), nullable=True),
        sa.Column("genres", mysql.TEXT(), nullable=True),
        sa.Column(
            "created_at",
            mysql.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            mysql.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("books")
