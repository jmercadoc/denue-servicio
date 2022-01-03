import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "../../")
sys.path.append(topdir)
from main import app
from flask import json

def test_states():
    response = app.test_client().get('/api/v1/estados/zacatecas/negocios')
    assert response.status_code == 200

def test_business_type():
    response = app.test_client().get('/api/v1/estados/zacatecas/negocios/restaurantes')
    assert response.status_code == 200

def test_one_municipality():
    response = app.test_client().get('/api/v1/estados/zacatecas/negocios/restaurantes?ubicacion=fresnillo')
    assert response.status_code == 200

def test_multiple_municipality():
    response = app.test_client().get('/api/v1/estados/zacatecas/negocios/restaurantes?ubicacion=fresnillo&ubicacion=guadalupe&ubicacion=jerez')
    assert response.status_code == 200

def test_variables_no_case_sensitive():
    response = app.test_client().get('/api/v1/estados/ZAcateCas/negocios/ZapaterIas?ubicacion=fREsnillO')
    assert response.status_code == 200

def test_filter_location():
    response = app.test_client().get('/api/v1/estados/zacatecas/negocios/zapaterias?ubicacion=fresnillo')
    data = json.loads(response.get_data())
    validate = [element for element in data[0]['fresnillo'] if 'fresnillo' not in element['Ubicacion'].lower()]
    assert len(validate) == 0
