import re
from flask import Flask, request, jsonify, Blueprint, make_response
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_raw_jwt)
from ..models import users
from ..models.users import USERS_LIST
from ..utils import _iterator

auth = Blueprint('auth', __name__, url_prefix='/api/v1')

BLACKLIST = set()
User = users.Users()
@auth.route('/users', methods=['GET'])
def get_all_users():
    '''Endpoint to get all users'''

    response = make_response(jsonify(User.get_all_users()))
    response.status_code = 200
    return response
