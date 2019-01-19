import os

from weight.db import Base, engine

from weight.db.models import WeightData

Base.metadata.create_all(engine)

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# from alembic.config import Config
# from alembic import command
# alembic_cfg = Config(f"{BASE_PATH}/alembic.ini")
# command.stamp(alembic_cfg, "head")
