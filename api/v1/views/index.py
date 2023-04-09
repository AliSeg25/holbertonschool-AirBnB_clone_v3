#!/usr/bin/python3
"""
app
"""

from flask import jsonify
import sys
sys.path.append("/home/ali/holbertonschool-AirBnB_clone_v3")
sys.path.append("/home/ali/holbertonschool-AirBnB_clone_v3")
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route("/status", methods=["GET"])
def get_status():
    return jsonify({"status": "OK"})


@app_views.route("/api/v1/stats", methods=["GET"])
def get_stats():
    """Permet de recupere tout les class dans un dict et le nombre instance"""
    stats = {}
    for cls in storage.classes().values():
        stats[cls.__name__.lower() + "s"] = storage.count(cls)
    return jsonify(stats)
