import requests
from os import environ
from dotenv import load_dotenv
from src.models.APIError import APIError

load_dotenv()
WSCATGEO_URL = environ.get('WSCATGEO_URL')

def searchStateByName(state):
    url = f'{WSCATGEO_URL}/mgee/buscar/{state}'
    response = requests.get(url).json()
    if 'datos' in response:
        return response['datos'][0]['cve_agee']
    else:
        raise APIError('El texto no existe en los nombres de las entidades.', 
        'Revise el nombre del estado ingresado', 404)
