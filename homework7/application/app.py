#!/usr/bin/env python3.9

import json
import os

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


app_data = {}
user_id_seq = 1


@app.route('/add_user', methods=['POST'])
def create_user():
    global user_id_seq

    user_name = json.loads(request.data)['name']
    if user_name not in app_data:
        app_data[user_name] = user_id_seq
        user_id_seq += 1
        return jsonify({'user_id': app_data[user_name]}), 201

    else:
        return jsonify(f'User_name {user_name} already exists: id: {app_data[user_name]}'), 400


@app.route('/get_user/<name>', methods=['GET'])
def get_user_id_by_name(name):
    if user_id := app_data.get(name):

        mock_host = os.environ['MOCK_HOST']
        mock_port = os.environ['MOCK_PORT']

        surname = None
        try:
            response = requests.get(f'http://{mock_host}:{mock_port}/get_surname/{name}')
            if response.status_code == 200:
                surname = response.json()
            else:
                print(f'No surname found for user {name}')
        except Exception as e:
            print(f'Unable to get surname from external system:\n{e}')

        data = {'user_id': user_id,
                'surname': surname
                }

        return jsonify(data), 200
    else:
        return jsonify(f'User_name {name} not found'), 404


@app.route('/update_user/<name>', methods=['PUT'])
def update_user(name):
    user_id = app_data.get(name)
    surname = json.loads(request.data)['surname']

    if user_id:
        mock_host = os.environ['MOCK_HOST']
        mock_port = os.environ['MOCK_PORT']
        try:
            resp = requests.put(f'http://{mock_host}:{mock_port}/put_surname/{name}', json={'surname': surname})
            if resp.status_code == 200:
                return jsonify(f'User {name} updated successfully'), 200

        except Exception as e:
            return jsonify(f'Unable to update user from external system:\n{e}'), 500

    return jsonify(f'User {name} not found'), 404


@app.route('/delete_surname/<name>', methods=['DELETE'])
def delete_surname(name):
    user_id = app_data.get(name)
    if user_id:
        mock_host = os.environ['MOCK_HOST']
        mock_port = os.environ['MOCK_PORT']

        try:
            resp = requests.delete(f'http://{mock_host}:{mock_port}/del_surname/{name}')
            if resp.status_code == 200:
                return jsonify(f'{name} was successfully deleted'), 200
            if resp.status_code == 422:
                return jsonify(f'User {name} does not have surname'), 422

        except Exception as e:

            return jsonify(f'Unable to delete surname from external system:\n{e}'), 500

        return jsonify('Unknown Error'), 520
    else:
        return jsonify(f'User name {name} not found'), 404


if __name__ == '__main__':
    host = os.environ.get('APP_HOST', '127.0.0.1')
    port = os.environ.get('APP_PORT', '4444')

    app.run(host, port)
