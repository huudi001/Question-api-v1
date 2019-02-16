import json
import datetime
from base_test import BaseTestCase

class TestQuestions(BaseTestCase):
    def test_get_questions_by_id(self):
        self.client.post('/api/v1/meetups', data=json.dumps(dict(meetup_id=1, location='mombasa',images='[image1, image2, image3]', topic='tech', tags='[data, sms, swahili pot]', happening_on='10/12/2018', created_on=str(datetime.datetime.now()) )), content_type='application/json')
        self.client.post('/api/v1/questions', data=json.dumps(dict(created_on=str(datetime.datetime.now()),question_id=1, created_by=1, meetup=2, title='tech', body='technology', votes=2)), content_type='application/json')
        result = self.client.get('/api/v1/questions/1')
        self.assertEqual(result.status_code,200)
