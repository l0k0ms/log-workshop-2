import requests

from flask import Flask, Response, jsonify
from flask import request as flask_request

from ddtrace import tracer, patch, config
from ddtrace.contrib.flask import TraceMiddleware

from bootstrap import create_app, db
from models import Network, Sensor

import random

sensors = []

# Tracer configuration
tracer.configure(hostname='agent')
tracer.set_tags({'env': 'workshop'})
patch(requests=True)

# enable distributed tracing for requests
# to send headers (globally)
config.requests['distributed_tracing'] = True

app = create_app()
traced_app = TraceMiddleware(app, tracer, service='sensors-api', distributed_tracing=True)

@app.route('/')
def hello():
    return Response({'Hello from Sensors': 'world'}, mimetype='application/json')

@app.route('/sensors', methods=['GET', 'POST'])
def get_sensors():
    if flask_request.method == 'GET':
        sensors = Sensor.query.all()
        system_status = []
        for sensor in sensors:
            system_status.append(sensor.serialize())
        return jsonify({'sensor_count': len(system_status),
                        'system_status': system_status})
    elif flask_request.method == 'POST':
        sensors.append({'sensor_no': len(sensors) + 1, 'value': random.randint(1,100)})
        return jsonify(sensors)
    else:
        err = jsonify({'error': 'Invalid request method'})
        err.status_code = 405
        return err

@app.route('/sensors/<id>/')
def sensor(id):
    return jsonify(Sensor.query.get(id).serialize())

@app.route('/refresh_sensors')
def refresh_sensors():
    sensors = simulate_all_sensors()
    return jsonify({'sensor_count': len(sensors),
                    'system_status': sensors})

@tracer.wrap(name='sensor-simulator')
def simulate_all_sensors():
    sensors = Sensor.query.all()
    for sensor in sensors:
        sensor.value = random.randint(1,100)
    db.session.add_all(sensors)
    db.session.commit()
    return [s.serialize() for s in sensors]