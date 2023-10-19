"""create activity table

Revision ID: 49c9cdce1d98
Revises: b88716f1fa59
Create Date: 2023-10-19 18:03:17.209081

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '49c9cdce1d98'
down_revision = 'b88716f1fa59'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        "activity",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("init_time", sa.DateTime(), nullable=True),
        sa.Column("end_time", sa.DateTime(), nullable=True),
        sa.Column("category_id", sa.Integer, nullable=False),
        sa.Column("post_id", sa.Integer, nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"],),
        sa.ForeignKeyConstraint(["post_id"], ["post.id"],),
        sa.ForeignKeyConstraint(["category_id"], ["category.id"],),
    )


def downgrade() -> None:
    op.drop_table("activity")
