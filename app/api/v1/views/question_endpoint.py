from flask import request, jsonify,  Blueprint
import datetime

from ..models.questions import QUESTIONS_LIST
from ..utils import get_by_key, _iterator, check_list


question = Blueprint('question', __name__, url_prefix='/api/v1')

Question = questions.Questions()

@question.route('/questions/<meetup_id>', methods=['GET'])
def get_all_questions(self,meetup_id):


        question = [questions for questions in QUESTIONS_LIST if questions['meetup'] == meetup_id]
        if  not  question:
            return {"message": "question for this meetup does not exist"}
        return question
