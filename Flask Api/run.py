from flask import Flask, request, jsonify,abort
import json
import api
from api import *
from api.views import app



if __name__ == '__main__':
    app.run(debug='True', port='5003')
                
                