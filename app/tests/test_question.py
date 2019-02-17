import json
import datetime
from base_test import BaseTestCase

class TestQuestions(BaseTestCase):

    def test_single_question(self):
          self.client.post('/api/v1/questions', data=json.dumps(dict(created_on=str(datetime.datetime.now()),question_id=1, created_by=1, meetup=2, title='tech', body='technology', votes=2)), content_type='application/json')
          result = self.client.get('/api/v1/questions/1')
          self.assertEqual(result.status_code,200)
