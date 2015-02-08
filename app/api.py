from app import app
from flask import request
from flask.ext.cors import cross_origin
import json

@app.route('/')
@cross_origin(origins="*")
def hello():
    return 'Hello World!'
