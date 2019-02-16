import datetime
from ..utils import get_by_key

MEETUPS_LIST = []


import datetime
class MeetUps():
    


    def get_meetup_by_id(self, meetup_id):
        meetup = get_by_key('meetup_id', meetup_id, MEETUPS_LIST)
        if not meetup:
            return {"message:" "meetup does not exist"}
        return meetup
