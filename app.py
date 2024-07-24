# app.py or wherever your Flask routes are defined
from flask import Flask, request, jsonify
from pydantic import ValidationError
from models.models import RequestModel, ResponseModel  # Importing the Event model
from ml_utils import make_recommendation
from http import HTTPStatus
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/recommend', methods=['POST'])
def handle_request():
    if request.json is None:
        return jsonify({"success": False, "error": "Empty request payload"}), HTTPStatus.BAD_REQUEST
    try:
        payload = RequestModel(**request.json)
        recommendations = make_recommendation(payload.data)
        response_data = ResponseModel(success=True, recommendations=recommendations)
        return jsonify(response_data.dict()), HTTPStatus.OK
    except ValidationError as e:
        logging.error(f"Validation error: {str(e)}")
        response_data = ResponseModel(success=False, error=str(e))
        return jsonify(response_data.dict()), HTTPStatus.BAD_REQUEST

def get_recommendations(data):
    return make_recommendation(data)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
