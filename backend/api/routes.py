from flask import Blueprint, request, jsonify
from model.loader import get_pipeline
from utils.cache import cache_answer

api_bp = Blueprint('api', __name__)

qa_pipeline = get_pipeline()

@api_bp.route('/answer', methods=['POST'])
def answer():
    try:
        data = request.get_json()
        question = data.get('question')
        context = data.get('context')
        if not question or not context:
            return jsonify({'error': 'Missing question or context'}), 400

        answer = cache_answer(question, context, qa_pipeline)
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
