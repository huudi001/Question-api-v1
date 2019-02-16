import json
import datetime
from base_test import BaseTestCase

class TestQuestions(BaseTestCase):
    def test_post_question(self):
        with self.client:
            response2 = self.client.post('/api/v1/questions', data=json.dumps(dict(created_on=str(datetime.datetime.now()),question_id=1, created_by=1, meetup=2, title='tech', body='technology', votes=2)), content_type='application/json')
            response_data = json.loads(response2.data)
            self.assertEqual("Question has been added successfully", response_data["message"])
            self.assertEqual(response2.status_code, 201)

            response = self.client.post('/api/v1/questions', data=json.dumps(dict(created_on=str(datetime.datetime.now()), created_by=1, question_id=1,meetup=2, title='', body='', votes=2)), content_type='application/json')
            response_data = json.loads(response.data)
            self.assertEqual("Some required fields are missing!", response_data["message"])
            self.assertEqual(response.status_code, 206)
            empty_response = self.client.post('/api/v1/questions', data=json.dumps(dict()),content_type='application/json')
            response_data = json.loads(empty_response.data)
            self.assertEqual("Fields cannot be empty",response_data["message"])
            self.assertEqual(empty_response.status_code, 400)
