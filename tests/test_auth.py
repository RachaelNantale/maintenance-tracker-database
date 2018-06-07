import json
import flask
from flask import jsonify
from run import app
import unittest
from dbHandler import MyDatabase

# def test_decode_token():
# 	user = MyDatabase.create_user(
# 		username= 'rachael@gmail.com',
# 		password='123abc')

# 	db.session.add(user)
# 	db.session.commit()
# 	token = user.encode.token(user.id)
# 	self.assertTrue(isinstance(token,bytes))
# 	self.assertTrue(UserModel,test_decode_token(token)==1)


class TestAuthBlueprint(unittest.TestCase):
	pass

	def setUp(self):
		self.client = app.test_client

	def test_register(self):
		"""Test for registration"""
		response = self.client().post(
				'/auth/register',
				data=json.dumps(dict(
					email='rachael@gmail.com',
					password='123abc')),
				content_type='application/json')
		data = json.loads(response.data.decode())
		self.assertTrue(data['status'] == 'success')
		self.assertTrue(data['message'] == 'Succesfully registered')
		self.assertTrue(data['token'])
		self.assertEqual(response.status_code, 201)

	def tearDown(self):
		"""
		Drop the data
		"""


if __name__ == '__main__':
	unittest.main()
