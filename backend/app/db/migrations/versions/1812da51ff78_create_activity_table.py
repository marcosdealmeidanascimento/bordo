"""create activity table

Revision ID: 1812da51ff78
Revises: f8aef32a4435
Create Date: 2023-08-25 16:07:32.957847

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '1812da51ff78'
down_revision = 'f8aef32a4435'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "activity",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("start_time", sa.Time(), nullable=False),
        sa.Column("category_id", sa.Integer, nullable=False),
        sa.Column("completion_time", sa.Time(), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("logbook_id", sa.Integer, nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"],),
        sa.ForeignKeyConstraint(["logbook_id"], ["logbook.id"],),
        sa.ForeignKeyConstraint(["category_id"], ["category.id"],),
    )


def downgrade() -> None:
    op.drop_table("activity")

