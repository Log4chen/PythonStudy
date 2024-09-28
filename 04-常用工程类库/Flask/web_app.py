import json

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route("/getUser")
def getUser():
    return {
        'username': 'tony',
        'age': 10
    }

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(obj):
        return json.dumps(User('tony', 10).to_dict())

if __name__ == "__main__":
    app.run()