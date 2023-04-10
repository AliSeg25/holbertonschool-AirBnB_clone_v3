#!/usr/bin/python3
"""
app
"""
import sys
from flask import Flask
from models import storage
from api.v1.views import app_views
import os
from flask import jsonify, make_response
from flask_cors import CORS
sys.path.append("/home/ali/holbertonschool-AirBnB_clone_v3")


app = Flask(__name__)
"""
Cette commande définit une stratégie de contrôle d'accès
à l'origine (CORS) pour l'application Flask. Cela signifie
que les requêtes provenant de domaines différents seront
autorisées à accéder aux ressources de l'API.
"""
CORS(app)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

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
