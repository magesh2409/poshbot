from flask import jsonify
from werkzeug.exceptions import HTTPException


def register_error_handler(app):
    @app.errorhandler(Exception)
    def handle_exception(e):
        if isinstance(e, HTTPException):
            code = e.code
            name = e.name
            description = e.description
        else:
            code = 500
            name = e.__class__.__name__
            description = str(e)

        return jsonify({
            "error": {
                "code": code,
                "type": name,
                "message": description
            }
        }), code