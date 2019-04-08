""" Main app views file."""
from flask import Flask, redirect
from flask import jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from .email_views import email_bp
from .user_views import auth_bp
from .group_views import group_bp

def create_app():
    """
    App factory for the epic mail app.
    """
    API_URL = "https://app.swaggerhub.com/apis-docs/GreatestCoderEverApi/Epic-mail/1.0.0"
    swagger_ui_bp = get_swaggerui_blueprint("/api/v2/docs", API_URL)    
    app = Flask(__name__)
    # Allow CORS for all routes
    CORS(app)

    app.register_blueprint(auth_bp, url_prefix='/api/v2/auth')
    app.register_blueprint(email_bp, url_prefix='/api/v2')
    app.register_blueprint(group_bp, url_prefix='/api/v2')
    app.register_blueprint(swagger_ui_bp, url_prefix="/api/v2/docs")

    @app.errorhandler(404)
    def page_not_found(e):
        """ Error handler route bad requests."""

        return jsonify({
            'status': 404,
            'data': [
                {
                    'Issue': "You have entered an unknown URL. NOTE all urls have a 'api/v1/' prefix.",
                    'message': 'Please do contact Derrick Sekidde for more details on this.'
                }]
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        """ This is a route handler for wrong methods."""

        return jsonify({
            "status": 405,
            "error": "The used method is not allowed for this endpoint. Change method or contact Derrick Sekidde."
        }), 405

    @app.route('/')
    @app.route('/api/v2')
    def home():
        return redirect("https://neelxie.github.io/epic-mail/UI/index.html")


    return app