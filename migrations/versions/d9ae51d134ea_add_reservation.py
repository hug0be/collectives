"""add_reservation

Revision ID: d9ae51d134ea
Revises: 78eeaa194828
Create Date: 2022-01-18 17:21:03.178179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9ae51d134ea'
down_revision = '78eeaa194828'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('collect_date', sa.DateTime(), nullable=False),
    sa.Column('return_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Enum('Planned', 'Ongoing', 'Completed', 'Cancelled', name='reservationstatus'), nullable=False),
    sa.Column('extended', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reservations_collect_date'), 'reservations', ['collect_date'], unique=False)
    op.create_index(op.f('ix_reservations_return_date'), 'reservations', ['return_date'], unique=False)
    op.create_table('reservation_lines',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('equipment_type_id', sa.Integer(), nullable=True),
    sa.Column('reservation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['equipment_type_id'], ['equipment_types.id'], ),
    sa.ForeignKeyConstraint(['reservation_id'], ['reservations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reservation_lines_equipments',
    sa.Column('reservation_line_id', sa.Integer(), nullable=False),
    sa.Column('equipment_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['equipment_id'], ['equipments.id'], ),
    sa.ForeignKeyConstraint(['reservation_line_id'], ['reservation_lines.id'], ),
    sa.PrimaryKeyConstraint('reservation_line_id', 'equipment_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation_lines_equipments')
    op.drop_table('reservation_lines')
    op.drop_index(op.f('ix_reservations_return_date'), table_name='reservations')
    op.drop_index(op.f('ix_reservations_collect_date'), table_name='reservations')
    op.drop_table('reservations')
    # ### end Alembic commands ###
