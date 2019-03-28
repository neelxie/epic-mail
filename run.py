""" This file runs the epic mail app."""

from app.views.app_views import create_app
from app.models.db import DatabaseConnection

app = create_app() # return app
db = DatabaseConnection()

if __name__ == '__main__':
    app.run(debug=False)
    db.create_db_tables()