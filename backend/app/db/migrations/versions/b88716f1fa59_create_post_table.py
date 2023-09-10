"""create post table

Revision ID: b88716f1fa59
Revises: f8aef32a4435
Create Date: 2023-09-10 14:21:50.370017

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'b88716f1fa59'
down_revision = 'f8aef32a4435'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "post",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("date", sa.Date(), nullable=True),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("logbook_id", sa.Integer, nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"],),
        sa.ForeignKeyConstraint(["logbook_id"], ["logbook.id"],),
    )


def downgrade() -> None:
    op.drop_table("post")
