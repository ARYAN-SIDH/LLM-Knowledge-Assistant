from flask import Flask
from flask_cors import CORS
from api.routes import api_bp
from utils.logger import setup_logger

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    CORS(app)

    # Register API blueprint
    app.register_blueprint(api_bp, url_prefix='/api')

    # Setup logger
    setup_logger(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
