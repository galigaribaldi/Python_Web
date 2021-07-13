from flask_restful import Api
from hello_world import HelloWorld

api = Api(app)
api.add_resource(HelloWorld, '/api')