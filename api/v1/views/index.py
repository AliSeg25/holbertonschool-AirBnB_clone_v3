#!/usr/bin/python3
"""
app
"""

from flask import jsonify
import sys
from api.v1.views import app_views
sys.path.append("/home/ali/holbertonschool-AirBnB_clone_v3")


@app_views.route("/status", methods=["GET"])
def get_status():
    return jsonify({"status": "OK"})
