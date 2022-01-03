class APIError(Exception):
    status_code = 400

    def __init__(self, message, suggestion, status_code=400, payload=None):
        super().__init__()
        self.message = message,
        self.suggestion = suggestion,
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
