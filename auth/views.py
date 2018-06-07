from flask import Blueprint, request, make_response, jsonify
from api.models import UserModel
import dbHandler
from dbHandler import MyDatabase


auth_blueprint = Blueprint('auth', __name__)


# add this to an init
class RegisterAPI():
    """
    Register a user
    """


db = MyDatabase


def post(self):
    post_data = request.get_json()
    user = db.create_user_table(username=post_data.get('username')).first
    if not user:
        try:
            user = User(
                username=post_data.get('username'),
                password=post_data.get('password')
            )

            # insert user
            db.session.add(user)
            db.session.commit()
            # generate token
            token = user.encode_token(user.id)
            responseObject = {
                'status': 'success',
                'message': 'Succesfully registered',
                'token': token.decode()
            }
            return make_response(jsonify(responseObject)), 201
        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'an error occured please try again.'
            }
        return make_response(jsonify(responseObject)), 401
    else:
        responseObj = {
            'status': 'fail',
            'message': 'User already exists. Please Log in'

        }
        return make_response(jsonify(responseObj)), 202


# define Api resourcex
registration_view = RegisterAPI('register_api')

# Add rules for the API end points
auth_blueprint.add_url_rule(
    '/auth/register',
    view_func=registration_view,
    methods=['POST'])
