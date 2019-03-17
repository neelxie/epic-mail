""" Main app views file."""
from flask import Flask
# from .mail_views import mail_bp
from .user_views import auth_bp

def create_app():
    """
    App factory for the epic mail app.
    """
    app = Flask(__name__)
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    # app.register_blueprint(mail_bp, url_prefix='/api/v1')

    return app