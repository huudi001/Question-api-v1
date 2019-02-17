from ..utils import get_by_key
import datetime

QUESTIONS_LIST = []



class Questions():

    def patch2(self,question_id):

        question= [questions for questions in QUESTIONS_LIST if questions['question_id'] == question_id]
        if  not question:
            return {"message":"question is not available"}
        question[0]['votes']-=1
