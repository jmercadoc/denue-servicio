from flask import Flask
from flasgger import Swagger
from src.routes.api.v1.Errors import errors
from src.routes.api.v1.Business import business
from src.docs.swagger import template, swagger_config

app = Flask(__name__)

Swagger(app, config=swagger_config, template=template)

app.register_blueprint(errors)
app.register_blueprint(business)
app.config['JSON_SORT_KEYS'] = False

if(__name__ == '__main__'):
    app.run(debug=True)
