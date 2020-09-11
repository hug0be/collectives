"""Add technician role

Revision ID: 9a774b0ca49b
Revises: f559a516d597
Create Date: 2020-06-15 22:16:56.475732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9a774b0ca49b"
down_revision = "fd21f2ac4136"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("roles", schema=None) as batch_op:
        batch_op.alter_column(
            "role_id",
            type_=sa.Enum(
                "Moderator",
                "Administrator",
                "President",
                "EventLeader",
                "ActivitySupervisor",
                "Technician",
                name="roleids",
            ),
            existing_type=sa.Enum(
                "Moderator",
                "Administrator",
                "President",
                "EventLeader",
                "ActivitySupervisor",
                name="roleids",
            ),
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("roles", schema=None) as batch_op:
        batch_op.alter_column(
            "role_id",
            existing_type=sa.Enum(
                "Moderator",
                "Administrator",
                "President",
                "EventLeader",
                "ActivitySupervisor",
                "Technician",
                name="roleids",
            ),
            type_=sa.Enum(
                "Moderator",
                "Administrator",
                "President",
                "EventLeader",
                "ActivitySupervisor",
                name="roleids",
            ),
        )

    # ### end Alembic commands ###