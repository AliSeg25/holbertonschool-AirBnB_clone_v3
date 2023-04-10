#!/usr/bin/python3
"""
states.py
"""
import sys
from flask import Flask, jsonify, request, make_response
from models import storage
from api.v1.views import app_views
from flask import abort
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
sys.path.append("/home/ali/holbertonschool-AirBnB_clone_v3")
sys.path.append("/home/ali/holbertonschool-AirBnB_clone_v3")


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_places(city_id):
    """
    Retrieves the list of all Place objects of a City
    """
    city = storage.get(City, city_id)

    if not city:
        abort(404)

    places = [place.to_dict() for place in city.places]

    return jsonify(places)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """
    Return place special par rapporr id
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """
    Deletes a Place Object
    """

    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    storage.delete(place)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def post_place(city_id):
    city = storage.get("City", city_id)
    if city is None:
        return jsonify({"error": "City not found"}), 404

    content = request.get_json()
    if content is None:
        return jsonify({"error": "Not a JSON"}), 400

    if "user_id" not in content.keys():
        return jsonify({"error": "Missing user_id"}), 400

    user = storage.get("User", content["user_id"])
    if user is None:
        return jsonify({"error": "User not found"}), 404

    if "name" not in content.keys():
        return jsonify({"error": "Missing name"}), 400

    place = Place(name=content["name"], city_id=city_id, user_id=content["user_id"])
    storage.new(place)
    storage.save()
    return jsonify(place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def put_place(place_id):
    """
    Updates a Place
    """
    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    non = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in non:
            setattr(place, key, value)
    storage.save()
    return make_response(jsonify(place.to_dict()), 200)
