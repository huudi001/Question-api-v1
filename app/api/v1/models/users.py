import string
import datetime as dt
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from ..utils import get_by_key, check_list

USERS_LIST = []


class Users():
    def get_all_users(self):
        result = check_list(USERS_LIST)
        return result
