from ..utils import get_by_key
import datetime

QUESTIONS_LIST = []



class Questions():

    def get_single_question(self, question_id):
        question = get_by_key('question_id', question_id, QUESTIONS_LIST)
        if not question:
            return {"message": "question does not exist"}
        return question
