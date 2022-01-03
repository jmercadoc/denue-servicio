template = {
    "swagger": "2.0",
    "info": {
        "title": "Consulta Negocios",
        "description": "API que proporciona la información de los negocios por localidades (Municipio/Delegación) del INEGI, DENUE",
        "version": "1.0"
    },
    "basePath": "/api/v1",
    "schemes": [
        "http",
        "https"
    ],
}

swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}
