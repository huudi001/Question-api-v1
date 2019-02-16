from flask import request, jsonify,  Blueprint
from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
import datetime
from ..models import meetups
from ..models.meetups import MEETUPS_LIST
from ..utils import get_by_key, _iterator


meetup = Blueprint('meetup', __name__, url_prefix='/api/v1')

MeetUp = meetups.MeetUps()


@meetup.route('/meetups/<int:meetup_id>', methods=['GET'])
#@jwt_required
def get_single_meetup(meetup_id):

    response = jsonify(MeetUp.get_meetup_by_id(meetup_id))
    response.status_code = 200
    return response
