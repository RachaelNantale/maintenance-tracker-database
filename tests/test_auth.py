import json
import flask
from flask import jsonify
from run import app
import unittest
from dbHandler import MyDatabase


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
