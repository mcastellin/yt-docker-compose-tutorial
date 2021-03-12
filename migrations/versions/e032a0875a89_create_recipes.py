"""create recipes

Revision ID: e032a0875a89
Revises: 
Create Date: 2020-06-22 12:00:28.111761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e032a0875a89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('ingredients', sa.UnicodeText(), nullable=True),
    sa.Column('directions', sa.UnicodeText(), nullable=True),
    sa.Column('createdts', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_recipe_createdts'), 'recipe', ['createdts'], unique=False)
    op.create_index(op.f('ix_recipe_name'), 'recipe', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_recipe_name'), table_name='recipe')
    op.drop_index(op.f('ix_recipe_createdts'), table_name='recipe')
    op.drop_table('recipe')
    # ### end Alembic commands ###
