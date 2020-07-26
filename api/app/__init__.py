from flask import Flask, Blueprint
from flask_restx import Api
from flask_cors import CORS

# Get the app initialized and set CORS rules
app = Flask(__name__)
blueprint = Blueprint("api", __name__, url_prefix="/api/v1.0")
api = Api(
    blueprint,
    title="Notes App API",
    version="v1.0",
    description="RESTful API for the Notes app",
    doc="/swagger",
)
app.register_blueprint(blueprint)
CORS(app, resources={r"/*": {"origins": "*"}})

from app import routes
