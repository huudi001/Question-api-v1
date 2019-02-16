import json
import datetime
from base_test import BaseTestCase

class TestMeetups(BaseTestCase):





    def test_single_meetup(self):
        self.client.post('/api/v1/meetups', data=json.dumps(dict(meetup_id=1, location='mombasa',images='[image1, image2, image3]', topic='tech', tags='[data, sms, swahili pot]', happening_on='10/12/2018', created_on=str(datetime.datetime.now()) )), content_type='application/json')
        result = self.client.get('/api/v1/meetups/1')
        self.assertEqual(result.status_code, 200)
