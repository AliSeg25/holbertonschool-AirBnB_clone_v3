#!/usr/bin/python3
"""
app
"""

from flask import jsonify
import sys
from api.v1.views import app_views
from models import storage
sys.path.append("/home/ali/holbertonschool-AirBnB_clone_v3")
sys.path.append("/home/ali/holbertonschool-AirBnB_clone_v3")


@app_views.route("/status", methods=["GET"])
def get_status():
    return jsonify({"status": "OK"})


@app_views.route("/api/v1/stats", methods=["GET"])
def get_stats():
    stats = {}
    for cls in storage.classes().values():
        stats[cls.__name__.lower() + "s"] = storage.count(cls)
    return jsonify(stats)
