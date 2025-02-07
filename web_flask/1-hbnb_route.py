#!/usr/bin/python3
""" Starts a Flash Web Application HBNB"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns a Message when it is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns a Message 'HBNB' when is called """
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

