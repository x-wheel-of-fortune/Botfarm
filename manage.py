from alembic.config import Config
from alembic import command

alembic_cfg = Config("alembic.ini")

if __name__ == "__main__":
    command.upgrade(alembic_cfg, "head")
