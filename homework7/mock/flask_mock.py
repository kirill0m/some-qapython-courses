#!/usr/bin/env python3.9

import threading
import json
import settings
from flask import Flask, jsonify, request

app = Flask(__name__)


SURNAME_DATA = {}


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    if surname := SURNAME_DATA.get(name):
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user "{name}" not found'), 404


def shutdown_stub():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_stub()
    return jsonify(f'Ok, exiting'), 200


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })

    server.start()
    return server


@app.route('/put_surname/<name>', methods=['PUT'])
def put_user_surname(name):
    surname = json.loads(request.data)['surname']
    actual_surname = SURNAME_DATA.get(name)

    SURNAME_DATA[name] = surname

    if actual_surname:
        return jsonify(f'{name} was successfully updated'), 200
    else:
        return jsonify(f'Unknown error'), 520


@app.route('/del_surname/<name>', methods=['DELETE'])
def del_user_surname(name):
    surname = SURNAME_DATA.get(name)

    if surname:
        del SURNAME_DATA[name]
        return jsonify(f'{name} was successfully deleted'), 200
    else:
        return jsonify(f'User {name} does not have surname'), 404
