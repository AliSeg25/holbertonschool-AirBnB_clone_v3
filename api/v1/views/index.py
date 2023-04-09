#!/usr/bin/python3
from flask import jsonify
import sys
sys.path.append("/home/ali/holbertonschool-AirBnB_clone_v3")
from api.v1.views import app_views


@app_views.route("/status", methods=["GET"])
def get_status():
    return jsonify({"status": "OK"})
