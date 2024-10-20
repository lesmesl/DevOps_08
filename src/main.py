from flask import Flask, jsonify
from src.database import init_db
from src.blueprints.blacklist import _blueprint
from src.errors.errors import ApiError
from src.utils.environment_config import load_environment_variables

load_environment_variables()

def setup_app():
    app = Flask(__name__)
    app.register_blueprint(_blueprint)

    @app.errorhandler(ApiError)
    def handle_error(err):
        response = {
            "msg": err.description if err.description else str(err),
        }
        return jsonify(response), err.code

    return app

app = setup_app()
init_db()

if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0")