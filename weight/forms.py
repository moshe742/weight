from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, SubmitField
from wtforms.validators import DataRequired


class WeightForm(FlaskForm):
    date = DateField('date', validators=[DataRequired()])
    old_weight = FloatField('old weight')
    new_weight = FloatField('new weight')
    submit = SubmitField('add weight')
