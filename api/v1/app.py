#!/usr/bin/python3
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

# create a variable app, instance of Flask
app = Flask(__name__)


"""
L'enregistrement du blueprint app_views avec l'instance
Flask appsignifie que les routes définies dans ce
blueprint seront disponibles pour l'application Flask
"""
app.register_blueprint(app_views)

"""
déclarer une méthode pour gérer @app.teardown_appcontext
qui appelle storage.close()@app.teardown_appcontext est
un décorateur de Flask qui indiquequ'une fonction doit
être appelée à la fin de chaque requête HTTP.
En utilisant cette déclaration, vous pouvez
être sûr que la connexion
avec le stockage sera toujours fermée correctement.
"""
@app.teardown_appcontext
def close_db(error):
    storage.close()


if __name__ == "__main__":
    # host = variable d'environnement HBNB_API_HOST ou 0.0.0.0 si non défini
    host = os.getenv("HBNB_API_HOST") or "0.0.0.0"
    # port = variable d'environnement HBNB_API_PORT ou 5000 si non défini
    port = int(os.getenv("HBNB_API_PORT") or 5000)
    threaded = True
    app.run(host=host, port=port, threaded=threaded)
