from flask import request, jsonify,  Blueprint
import datetime
from ..models import meetups
from ..models.meetups import MEETUPS_LIST
from ..utils import get_by_key, _iterator


meetup = Blueprint('meetup', __name__, url_prefix='/api/v1')

MeetUp = meetups.MeetUps()
@meetup.route('/meetups/<upcoming>', methods=['GET'])
def get_upcoming(self,upcoming):
    upcoming = datetime.datetime.now().isoformat()

    meetup = [meetups for meetups in MEETUPS_LIST if meetups['happening_on'] > upcoming]
    return MeetUps
