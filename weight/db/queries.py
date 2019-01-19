from datetime import datetime

from weight.db import SessionScope
from weight.db.models import WeightData


def get_weight_data(session, id):
    return session.query(WeightData).filter_by(id=id).first()


def get_weights_data(session):
    return session.query(WeightData).order_by(WeightData.date).all()


def add_weight_data(data, session):
    date = datetime.now()
    if data['date']:
        date = data['date']
    weight_data = WeightData(date=date,
                             old_weight=data['old_weight'],
                             new_weight=data['new_weight'])
    session.add(weight_data)
    return weight_data


def edit_weight_data(data, session, id):
    weight_to_edit = session.query(WeightData).filter_by(id=id).first()
    for key, val in data.items():
        setattr(weight_to_edit, key, val)
    return weight_to_edit


def delete_weight_data(data, session):
    weight_to_delete = session.query(WeightData).filter_by(id=data['id']).first()
    session.delete(weight_to_delete)
    return weight_to_delete
