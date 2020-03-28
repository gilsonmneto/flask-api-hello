"""Flask API Hello World"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/hello')  # http://127.0.0.1:8001/hello

if __name__ == "__main__":
    app.run(port=8001, debug=True)
