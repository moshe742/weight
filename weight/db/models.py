from weight.db import Base
from sqlalchemy import Column, Integer, Date, Float


class WeightData(Base):
    __tablename__ = 'weight_data'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    old_weight = Column(Float)
    new_weight = Column(Float, nullable=True)

    def __repr__(self):
        return f"<WeightData(id={self.id}, date={self.date}, " \
            f"old weight={self.old_weight})>"

    def __str__(self):
        return f"date: {self.date}, old weight: {self.old_weight}"
