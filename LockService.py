from flask_api import FlaskAPI
from flask import request
import base64
import json


app = FlaskAPI(__name__)


locked_files = []


@app.route('/lock', methods=['POST'])
def lock():
    new_file = request.json
    for file in locked_files:
        if file['filename'] == new_file['filename']:
            return json.dumps(True)
    locked_files.append(new_file)
    return json.dumps(False)


@app.route('/unlock', methods=['POST'])
def unlock():
    new_file = request.json
    for file in locked_files:
        if file['filename'] == new_file['filename']:
            locked_files.remove(file)
            return 'File unlocked.'


@app.route('/check/<filename>', methods=['GET'])
def check_owner(filename):
    for file in locked_files:
        if file['filename'] == filename:
            return str(filename + " is locked by user " + file['userId'])
    return 'This file is either not locked or does not exist.'

if __name__=='__main__':
    app.run(port=8003)