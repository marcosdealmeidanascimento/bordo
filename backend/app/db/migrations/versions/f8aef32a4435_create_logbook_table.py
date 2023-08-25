"""create logbook table

Revision ID: f8aef32a4435
Revises: 49e400160ced
Create Date: 2023-08-25 13:28:04.422902

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'f8aef32a4435'
down_revision = '49e400160ced'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "logbook",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"],),
    )


def downgrade() -> None:
    op.drop_table("logbook")
