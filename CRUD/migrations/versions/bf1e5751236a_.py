"""empty message

Revision ID: bf1e5751236a
Revises: 
Create Date: 2019-08-12 11:16:17.097002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf1e5751236a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('temas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('color', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('color')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.Text(), nullable=True),
    sa.Column('descricao', sa.Text(), nullable=True),
    sa.Column('tema_cor', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tema_cor'], ['temas.color'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('temas')
    # ### end Alembic commands ###
