#!/usr/bin/python3
"""
states.py
"""
from flask import Flask, jsonify, request, make_response
from models import storage
from api.v1.views import app_views
import sys
from flask import abort
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
sys.path.append("/home/ali/holbertonschool-AirBnB_clone_v3")
sys.path.append("/home/ali/holbertonschool-AirBnB_clone_v3")


@app_views.route('/states/', methods=['GET'], strict_slashes=False)
def get_states():
    """Retrieves the list of all State objects"""
    states = storage.all("State").values()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """cette fonction permet de récupérer une instance
    spécifique avec un id pour la retrouver."""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def post_state():
    """
    Creates a State
    """
    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    # ** permet de faire passer args
    instance = State(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """Updates a State object"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    try:
        request_json = request.get_json()
    except:
        return jsonify({"error": "Not a JSON"}), 400
    if request_json is None:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in request_json.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """
    récupérer un objet d'état spécifique à partir de son ID 
    """
    state = storage.get(State, state_id)

    if not state:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    non = ['id', 'created_at', 'updated_at']

    # données requête récupérées
    data = request.get_json()

    for key, value in data.items():
        if key not in non:
            setattr(state, key, value)
    storage.save()

    return make_response(jsonify(state.to_dict()), 200)
