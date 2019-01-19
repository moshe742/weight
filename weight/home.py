import logging
from datetime import date
from flask import request, render_template, jsonify, redirect, url_for

from weight import app
from weight.db import SessionScope
from weight.forms import WeightForm
from weight.db.queries import (
    add_weight_data,
    edit_weight_data,
    delete_weight_data,
    get_weights_data,
    get_weight_data,
)

logging.basicConfig(filename='weight.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def get_weight():
    logger.info('start get weight')
    with SessionScope() as session:
        weights = get_weights_data(session)
        dates = []
        weight_data_old = []
        weight_data_new = []
        for item in weights:
            dates.append(item.date.strftime('%Y-%m-%d'))
            weight_data_old.append(item.old_weight)
            weight_data_new.append(item.new_weight)
        logger.info('return render template')
        return render_template('weight/index.html', weights=weights, weight_data_old=weight_data_old,
                               dates=dates, weight_data_new=weight_data_new)


@app.route('/get_weight_data')
def get_data_weight():
    logger.info('start get weight data')
    with SessionScope() as session:
        weights = get_weights_data(session)
        dates = []
        weight_data_old = []
        weight_data_new = []
        for item in weights:
            dates.append(item.date.isoformat())
            weight_data_old.append(item.old_weight)
            weight_data_new.append(item.new_weight)

        weight_data_old = {
            'x': dates,
            'y': weight_data_old,
            'mode': 'lines+markers',
            'name': 'old weight',
        }
        weight_data_new = {
            'x': dates,
            'y': weight_data_new,
            'mode': 'lines+markers',
            'name': 'new weight',
        }
        logger.info('return jsonify')
        return jsonify({
            'old_weight': weight_data_old,
            'new_weight': weight_data_new,
        })


@app.route('/add_weight', methods=['GET', 'POST'])
def add_weight():
    logger.info('start add weight')
    form = WeightForm()
    if form.validate_on_submit():
        with SessionScope() as session:
            add_weight_data(request.form, session)
        return redirect(url_for('get_weight'))
    else:
        logger.info('in else')
        form.date.data = date.today()
        logger.info('return render template')
        return render_template('weight/add_weight.html', form=form, change='add')


@app.route('/edit_weight/<id>', methods=['GET', 'POST'])
def edit_weight(id):
    form = WeightForm()
    if form.validate_on_submit():
        with SessionScope() as session:
            edit_weight_data(request.form, session, id)
        return redirect(url_for('get_weight'))
    else:
        with SessionScope() as session:
            try:
                weight_data = get_weight_data(session, id)
                form.date.data = weight_data.date
                form.old_weight.data = weight_data.old_weight
                form.new_weight.data = weight_data.new_weight
                return render_template('weight/add_weight.html', form=form, change='edit')
            except Exception as e:
                logging.info(str(e))
                return str(e)
