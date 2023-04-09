#!/usr/bin/python3
from flask import jsonify
import sys
sys.path.append("/home/ali/holbertonschool-AirBnB_clone_v3")
from api.v1.views import app_views

"""
Le fichier index.py permet de définir une vue pour votre
application Flask. Cette vue aura une route nommée "/status",
qui retournera un objet JSON avec la clé "status" et la valeur
"OK". Cette vue est enregistrée avec l'objet Blueprint app_views,
qui a été importé depuis le fichier api.v1.views.
"""
@app_views.route("/status", methods=["GET"])
def get_status():
    return jsonify({"status": "OK"})
