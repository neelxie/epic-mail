""" This file runs the epic mail app."""

from app.views.app_views import create_app

app = create_app() # return app

if __name__ == '__main__':
    app.run(debug=True)