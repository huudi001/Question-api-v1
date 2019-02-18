import json
import datetime
from base_test import  BaseTestCase
class Testauth(BaseTestCase):
    def test_get_all_users(self):
        # Register a user
        self.client.post(
            '/api/v1/register',
            data=json.dumps(dict(
                firstname='mohamed',
                lastname='hassan',
                othername='amiin',
                email='mary@gmail.com',
                phoneNumber='09877444',
                username='mary',
                password='1234',
                confirm_password='1234',
                isAdmin='true',
                registered=str(datetime.datetime.now())
            )),
            content_type='application/json'
        )
        result = self.client.get('/api/v1/users')
        self.assertEqual(result.status_code, 200)
