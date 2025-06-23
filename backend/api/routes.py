from flask import Blueprint, request, jsonify
from model.loader import get_pipeline
from model.prompt_handler import build_prompt  # ✅ import your custom builder

api_bp = Blueprint('api', __name__)

# Use a text-generation pipeline for custom prompts
llm_pipeline = get_pipeline()

@api_bp.route('/answer', methods=['POST'])
def answer():
    try:
        data = request.get_json()
        question = data.get('question')
        context = data.get('context')

        if not question or not context:
            return jsonify({'error': 'Missing question or context'}), 400

        # ✅ Build the custom prompt
        prompt = build_prompt(question, context)

        # ✅ Generate answer with prompt
        result = llm_pipeline(prompt, max_new_tokens=200, do_sample=True)[0]['generated_text']

        # ✅ Optionally, remove the prompt part from the result (depends on your model)
        answer = result.split('Answer:')[-1].strip()

        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
