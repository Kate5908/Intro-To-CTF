from flask import Flask
app = Flask(__name__)

from . import routes  # Assuming routes.py is correctly placed in the same board directory

def create_app():
    app = Flask(__name__)

    app.register_blueprint(routes.bp)

    return app