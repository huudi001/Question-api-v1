from unittest import TestCase
from app import create_app
from app.api.v1.models.users import  USERS_LIST


from app.api.v1.models.questions import QUESTIONS_LIST
from app.api.v1.models.meetups import  MEETUPS_LIST




class BaseTestCase(TestCase):

    def setUp(self):
        self.app = create_app(config="testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()


    def tearDown(self):


        del USERS_LIST[:]


        del QUESTIONS_LIST[:]
        del MEETUPS_LIST[:]
