from os import environ
from dotenv import load_dotenv
from flask import Blueprint, jsonify
from src.models.APIError import APIError

load_dotenv()
DOCS_URL = environ.get('DOCS_URL')
errors = Blueprint('errors', __name__)

@errors.app_errorhandler(APIError)
def handle_error(error):
    response = {
        'success': False,
        'error': {
            'type': error.__class__.__name__,
            'message': error.message
        },
        'suggestion': error.suggestion,
        'docs': f'{DOCS_URL}',
        'help': 'If you need help, email support@demo.com'
    }
    return jsonify(response), error.status_code

@errors.app_errorhandler(404)
def page_not_found(error):
    response = {
        'success': False,
        'error': {
            'type': error.__class__.__name__,
            'message': str(error)
        },
        'docs': f'{DOCS_URL}',
        'help': 'If you need help, email support@demo.com'
    }
    return jsonify(response), 404

@errors.app_errorhandler(500)
def page_not_found(error):
    response = {
        'success': False,
        'error': {
            'type': 'Internal Server Error',
            'message': 'Unable to handle this request'
        },
        'help': 'if the problem persists email support@demo.com'
    }
    return jsonify(response), 500
