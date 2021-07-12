from flask import Flask
from flask_restful import Api, Resource
from database import init_db
from views import UserViews


app = Flask(__name__)

api = Api(app)

@app.before_first_request
def init_app():
    init_db()

@api.resource('/')
class home(Resource):
    def get(self):
        return 'Hello Nexio!!!'

api.add_resource(UserViews, '/user/<string:user_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)