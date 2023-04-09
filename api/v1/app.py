#!/usr/bin/python3
"""
app
"""
import sys
sys.path.append("/home/ali/holbertonschool-AirBnB_clone_v3")
from flask import Flask
from models import storage
from api.v1.views import app_views
import os
from flask import jsonify, make_response


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    # host = variable d'environnement HBNB_API_HOST ou 0.0.0.0 si non défini
    host = os.getenv("HBNB_API_HOST") or "0.0.0.0"
    # port = variable d'environnement HBNB_API_PORT ou 5000 si non défini
    port = int(os.getenv("HBNB_API_PORT") or 5000)
    threaded = True
    app.run(host=host, port=port, threaded=threaded)
