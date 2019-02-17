from flask import request, jsonify,  Blueprint
import datetime
from ..models import questions
from ..models.questions import QUESTIONS_LIST
from ..utils import get_by_key, _iterator, check_list


question = Blueprint('question', __name__, url_prefix='/api/v1')

Question = questions.Questions()


@question.route('/questions/<int:question_id>/upvote', methods=['PATCH'])
def upvote(question_id):

    response = jsonify(Question.patch1(question_id))
    response.status_code = 200
    return response
