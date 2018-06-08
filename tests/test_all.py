import json
import flask
from flask import jsonify
from run import app
from flask_testing import TestCase
import unittest

#import requests


class TestClass(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client

    # #create a request

    def test_create_request(self):
        post_data = (
            {
                'requests': 'fix my car',
                'type': 'repair'
            }
        )

        response = self.client().post('/api/v1/users/requests',
                                      content_type='application/json', data=json.dumps(post_data))
        reply = json.loads(response.data.decode())
        if reply['requests'] == None:
            return jsonify({'message': 'Please fill in a request'})

        # self.assertEquals(reply['status'], 'OK')
        # self.assertEquals(reply['message'], 'A new request has been created')
        self.assertEqual(response.status_code, 201)

    # # #modify a request
    def test_modify_request(self):
        response = self.client().post(
            '/api/v1/auth/login/',
            content_type='application/json',
            data=json.dumps((dict(
                            email='rachael@gmail.com',
                            password='123abc')))
            )
        reply = json.loads(response.data.decode())
        token = reply['token']
        response_2 = self.client().put(
            '/api/v1/users/requests/1',
            content_type='application/json',
            data=json.dumps(post_data = (
                {
                    'requests': '#123',
                    'type': 'this is a request'
                }),
            headers={'Authorization': token}))
        _reply = json.loads(response_2.data.decode())
        #self.assertEqual(reply['status'], 'OK')
        self.assertEqual(_reply['message'], 'A Request has been modified')
        self.assertEqual(_response.status_code, 200)

    # # # # #fetch all requests

    def test_fetch_all_requests(self):
        response = self.client().get('api/v1/users/requests',
                                     content_type='application/json')
        reply = json.loads(response.data.decode())
        self.assertEqual(reply['status'], 'OK')
        self.assertEqual(reply['message'], 'here are all your requests')
        self.assertEqual(response.status_code, 200)

    # fetch single id

    def test_fetch_single_id(self):
        response = self.client().get('/api/v1/users/requests/1/',
                                     content_type='application/json')
        reply = response.data
        # self.assertEqual(len(reply.fetch_requests),1)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
