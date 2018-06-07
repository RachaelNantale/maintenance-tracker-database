from flask import Flask, request, jsonify, abort, Blueprint, make_response
import json
from api.models import RequestModel, UserModel
from api.models import maintance_requests, user_list
import jwt
import datetime
import uuid
from functools import wraps
from dbHandler import MyDatabase
import os
# from flask_bcrpyt import Bcrpyt

app = Flask(__name__)


# create a token header


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        usermodel = UserModel('1', 'rachael', '123abc')

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({'token': token,  'message': 'Token is missing!!!!'}), 401

        try:
            token_split = token.split(".")
            data = jwt.decode(token, os.getenv('SECRET_KEY'))
            current_user = usermodel.get_id()

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Sorry Token doesnt exist'}), 401
        except jwt.ExpiredSignature:
            return jsonify({'message': 'the token has expired.'}), 401

        return f(current_user, *args, **kwargs)
    return decorated


# create a new request
@app.route('/api/v1/users/requests', methods=['POST'])
def create_request():
    """
                    This endpoint creates a maintance request ticket
    """
    data = request.get_json()

    _requests = data.get('requests'),
    if not _requests or _requests == '':
        return jsonify({'message': 'Missing information. Please fill in'}), 400
    _types = data.get('types')
    if _types == '':
        return jsonify({'message': 'Missing infor Please fill in'}), 400

    try:
        if isinstance(data['requests'], str) and isinstance(data['type'], str):
            id = len(maintance_requests)
            id += 1
            Request = RequestModel(id, data['requests'], data['type'])
            maintance_requests.append(Request)
        return jsonify(Request.get_dict()), 201
    # Add an Attribut error to catch the errors
    except AttributeError:
        return jsonify({
            'status': 'FAIL',
            'message': 'Failed to create a request. Invalid data'
        }), 400

# create an api endpoint for modifying requests


@app.route('/api/v1/users/requests/<id>', methods=['PUT'])
@token_required
def modify_request(current_user, id):
    if not current_user:
        return jsonify({'message: User can not collect all requests'})

    data = request.get_json()
    """
	This endpoint modifies a request
	"""
    _requests = data.get('requests')
    print(_requests)
    _types = data.get('type')
    if not _requests or _requests == ' ':
        return jsonify({'message': 'Missing information. Please fill in'}), 400
    _types = data.get('type')
    if not _types or _types == ' ':
        return jsonify({'message': 'Missing infor Please fill in'}), 400

    # try:
    if isinstance(data['requests'], str) and isinstance(data['type'], str):

        counter = 0
    for item in maintance_requests:
        if id == item['_id']:
            maintance_requests[counter] = counter
            return
            # maintance_requests[counter]
        counter = counter + 1
        requestss = RequestModel(id, data['requests'], data['type'])
        result = requestss.get_dict()
        return jsonify({
            "message": "Request Updated"
        }), 201
# except AttributeError, IndexError):
    return jsonify({
        'status': 'FAIL',
        'message': 'Failed to modify a request. Invalid data'
    }), 400

# create API endpoints for fetching all requests


@app.route('/api/v1/users/requests', methods=['GET'])
@token_required
def fetch_all_requests(current_user):
    data = request.get_json

    if not current_user:
        return jsonify({'message: User can not collect all requests'})

    count = len(maintance_requests)
    requestss = RequestModel(id, data['requests'], data['type'])

    return jsonify({
        'status': 'OK',
        'message': 'here are all your requests',
        'request_number': count,

        'requests': requestss.get_dict()

    }), 200

# create API endpoints for fecthind a single id


@app.route('/api/v1/users/requests/<requestID>/', methods=['GET'])
@token_required
def fetch_request_id(current_user, requestID):
    if not current_user:
        return jsonify({'message: User can not collect all requests'})

    fetch_requests = []
    data = maintance_requests
    if int(requestID) > len(data):
        return jsonify({
            'status': 'Fail',
            'message': 'ID not found. Please add a valid ID'

        }), 400
    obj = data[int(requestID)-1]
    fetch_requests.append(obj)

    return jsonify({
        'status': 'Success',
        'request': fetch_requests
    })


@app.route('/auth/login/', methods=['POST'])
def user_login():
    auth = request.json
    usermodel = UserModel('1', 'rachael', '123abc')

    if not auth or not auth['username'] or not auth['password']:
        return make_response('could not verifys', 401, {'WWW-Aunthenticate': 'Basic realm="Login required"'})

    # user = User.filter_by(name=auth.username).first()

    if not usermodel:
        return jsonify({'message': 'No user Found'})

    if (usermodel.get_password, auth['password']):
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat': datetime.datetime.utcnow(),
            'sub': usermodel.get_id()
        }
        token = jwt.encode(payload, os.getenv('SECRET_KEY'))
        return jsonify({'token': token.decode('utf-8')}), 201
    return make_response('Could not verify', 401, {'WWW-Aunthenticate': 'Basic realm="Login required"'})


@app.route('/api/v1/requests/<requestId>/approve', methods=['PUT'])
@token_required
def create_admin_approve(current_user):
    if not current_user.admin:
        return jsonify({'message: User can not collect all requests'})


@app.route('/api/v1/requests/<requestId>/disaprove', methods=['PUT'])
@token_required
def create_admin_disaprove(current_user):
    if not current_user.admin:
        return jsonify({'message: User can not collect all requests'})


@app.route('/api/v1/requests/<requestId>/resolve', methods=['PUT'])
@token_required
def create_admin_resolve(current_user):
    if not current_user.admin:
        return jsonify({'message: User can not collect all requests'})
