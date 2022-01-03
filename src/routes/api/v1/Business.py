import requests
from os import environ
from dotenv import load_dotenv
from flasgger import swag_from
from flask import Blueprint, jsonify, request
from src.services.Wscatgeo import searchStateByName

load_dotenv()
business = Blueprint('business', __name__, url_prefix='/api/v1/')
DENUE_URL = environ.get('DENUE_URL')
DENUE_TOKEN = environ.get('DENUE_TOKEN')

@business.get('/estados/<state>/negocios')
@business.get('/estados/<state>/negocios/<business_type>', endpoint='with-business')
@swag_from('../../../docs/business.yml', endpoint='business.with-business', methods=['GET'])
def bussinesMultiple(state, business_type='todos'):
    locations = request.args.getlist('ubicacion')
    state = searchStateByName(state)
    url = f'{DENUE_URL}/v1/consulta/BuscarEntidad/{business_type}/{state}/1/1000/{DENUE_TOKEN}'
    response = requests.get(url).json()
    result = filterLocation(response, locations) if len(locations) >= 1 else response
    return jsonify(result), 200

def filterLocation(values, locations):
    filtered = []
    for location in locations:
        data = [element for element in values if location.lower() in element['Ubicacion'].lower()]
        filtered.append({location: data})
    return filtered
