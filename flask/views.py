from database import db_session as db
from flask_restful import fields, marshal_with, reqparse, Resource
from models import User
from sqlalchemy import exists

class PhoneNumber(fields.Raw):
    def format(self, value):
        return value[0:4]+'-'+value[4:7]+'-'+value[7:]

class UserViews(Resource):

    resource_fields = {
        'name': fields.String,
        'job_title': fields.String,
        'communicate_information': {
            'email': fields.String,
            'mobile': PhoneNumber
        }
    }
    check_fields = ('job_title', 'email', 'mobile')
    create_parser = reqparse.RequestParser()
    update_parser = reqparse.RequestParser()
    for key in check_fields:
        create_parser.add_argument(key, required=True, help=f'Missing value {key}')
        update_parser.add_argument(key)

    @marshal_with(resource_fields, envelope='resource')
    def get(self, user_id):
        user = db.query(User).filter(User.name == user_id).first()
        return user

    def delete(self, user_id):
        user = db.query(User).filter(User.name == user_id).first()
        if user:
            db.delete(user)
            db.commit()
        return '', 204

    def post(self, user_id):
        args = self.create_parser.parse_args()
        if db.query(exists().where(User.name == user_id)).scalar():
            return f'{user_id} already exists', 200
        user = User(user_id, args['email'], args['job_title'], args['mobile'])
        db.add(user)
        db.commit()
        return f'create {user_id}', 201

    def patch(self, user_id):
        args = self.update_parser.parse_args()
        user = db.query(User).filter(User.name == user_id).first()
        user.email = args.get('email') or user.email
        user.job_title = args.get('job_title') or user.job_title
        user.mobile = args.get('mobile') or user.mobile
        db.commit()
        return f'update {user_id}', 201
