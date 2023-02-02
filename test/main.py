from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route('/register', methods=['POST'])
def login():
    return "YES"


if __name__ == '__main__':
    app.run(debug=True)
