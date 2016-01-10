"""empty message

Revision ID: 30f80ed0ba5b
Revises: None
Create Date: 2013-12-28 00:54:48.444000

"""

# revision identifiers, used by Alembic.
revision = '30f80ed0ba5b'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sound',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=120), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('theme_song',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=120), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('urole', sa.String(length=5), nullable=True),
    sa.Column('themesong_id', sa.Integer(), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['themesong_id'], ['theme_song.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nickname')
    )
    op.create_table('sound_tags',
    sa.Column('sound_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['sound_id'], ['sound.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint()
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sound_tags')
    op.drop_table('user')
    op.drop_table('tag')
    op.drop_table('theme_song')
    op.drop_table('sound')
    ### end Alembic commands ###
