from flask import Flask, request, jsonify, abort, Blueprint, make_response
import json
from api.models import RequestModel, UserModel
import jwt
import datetime
import uuid
from functools import wraps
from api.dbHandler import MyDatabase
import os
# from flask_bcrpyt import Bcrpyt

app = Flask(__name__)


# create a database hndler
db = MyDatabase()

#create a token decoder
def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None
		if 'Authorization' in request.headers:
			token = request.headers['Authorization']
		if token is None:
			return jsonify({'token': token,  'message': 'Token is missing!!!!'}), 401

		try:
			data = jwt.decode(token, "os.getenv('SECRET_KEY')")
			current_user = data['id']

		except jwt.ExpiredSignatureError:
			return jsonify({'message': 'Sorry Token doesnt exist'}), 401
		except jwt.ExpiredSignature:
			return jsonify({'message': 'the token has expired.'}), 401

		return f(current_user, *args, **kwargs)
	return decorated


# create a new user
@app.route('/api/v1/auth/signup', methods=['POST'])
def create_user():
	data = request.get_json()
	username = data.get('username',None)
	password = data.get('password',None)
	email = data.get('email',None)

	if username is not None and password is not None and email is not None:
		_id=str(uuid.uuid1())
		# Generate token
		payload = {
				'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
				'iat': datetime.datetime.utcnow(),
				'id': _id
			}
		token = jwt.encode(payload, "os.getenv('SECRET_KEY')").decode('utf-8')
		
		db.create_user(_id,username,password,email)
		return jsonify({'message':"User created sucessfully",'status':True, 'token':token}),201
	else:
		return jsonify({'message':"Please fill in all fields",'status':False}),401

# Create a  user login
@app.route('/api/v1/auth/login/', methods=['POST'])
def user_login():
	data = request.get_json()
	username = data['username']
	password=data['password']

	if username is not None and password is not None:
		_id = db.user_login(username)
		if _id is not None:
			payload = {
				'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
				'iat': datetime.datetime.utcnow(),
				'id': _id
			}

			token = jwt.encode(payload, "os.getenv('SECRET_KEY')")

			return jsonify({'message':'Login Succesfull', 'Status':True,'token': token.decode('utf-8')}), 201
		else:
			return jsonify({'message':'User doesnot exist', 'Status':False}), 401

	else:
		return jsonify({'message':'Login Failed', 'Status':False}), 401

# create a new request
@app.route('/api/v1/users/requests', methods=['POST'])
@token_required
def create_request(current_user):
   
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


	id = int(data['id'])

	requests = data['requests']
	mtype = data['type']
	status = data['status']
	user_id =current_user


	db.create_request("INSERT INTO RequestTable VALUES({},'{}','{}','{}','{}')".format(
		id, requests, mtype, status,user_id[0]))

	
	return jsonify({'message':"Request Created",'success':True}), 201
	
	return jsonify({
		'status': 'FAIL',
		'message': 'Failed to create a request. Invalid data'
		}), 400


# create an api endpoint for modifying requests
@app.route('/api/v1/users/requests/<_id>', methods=['PUT'])
@token_required
def modify_request(current_user, _id):
	if not current_user:
		return jsonify({'message: User can not collect all requests'})

	data = request.get_json()
	"""
	This endpoint modifies a request
	"""
	
	mid = data.get('_id',None)
	_id = mid
	requests = data.get('requests',None)
	mtype = data.get('Type',None)

	if _id is not None and requests is not None and mtype is not None:
		db = MyDatabase()
		db.modify_request("UPDATE RequestTable SET requests='{}', Type='{}'  WHERE id='{}' ".format(requests,mtype, _id))
		return jsonify({
				"message": "Request Updated", "status":"OK"
			}), 201
	else:
		return jsonify({"message":"All fields  are required"}),400



# Fetch all requests of the logged in user
@app.route('/api/v1/users/requests', methods=['GET'])
@token_required
def fetch_all_requests(current_user):
	result = db.fetch_all_requests_for_a_user(current_user)
	if result is not None:
	 	return jsonify(result)
	else:
		return jsonify({'message': 'You have no requests'}),200
	



	

@app.route('/api/v1/users/requests/<requestID>/', methods=['GET'])
@token_required
def fetch_request_id(current_user, requestID):
	result = db.fetch_one_user(requestID)
	if result is not None:
		
		return jsonify(result)
	else:
		return jsonify({'message': 'You have no requests'}),200 
	





#Approving a request by the admin
@app.route('/api/v1/requests/<requestId>/approve', methods=['PUT'])
@token_required
def create_admin_approve(current_user):
	if not current_user.admin:
		return jsonify({'message: User can not collect all requests'})


#Disaaproving a request by the admin
@app.route('/api/v1/requests/<requestId>/disaprove', methods=['PUT'])
@token_required
def create_admin_disaprove(current_user):
	if not current_user.admin:
		return jsonify({'message: User can not collect all requests'})


#Resolving  a request by the admin
@app.route('/api/v1/requests/<requestId>/resolve', methods=['PUT'])
@token_required
def create_admin_resolve(current_user):
	if not current_user.admin:
		return jsonify({'message: User can not collect all requests'})
