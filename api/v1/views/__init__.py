#!/usr/bin/python3
"""
flask.Blueprint est un objet utilisé pour organiser 
es parties logiques de votre application Flask.
Les applications Flask sont souvent divisées en plusieurs
parties, appelées "blueprints", pour une meilleure
organisation et une maintenance plus facile.
Chaque blueprint peut avoir ses propres routes,
modèles, vues, etc. Une fois que les blueprints
sont définis, ils peuvent être enregistrés auprès
de l'application Flask principale pour être utilisés.
"""
from flask import Blueprint

"""
créer une variable app_views qui est une instance de Blueprint
(le préfixe d'url doit être /api/v1)
cette déclaration crée un blueprint qui peut être enregistré
avec une instance de Flask pour ajouter un ensemble de routes
à votre application. Les routes seront préfixées avec "/api/v1"
pour les distinguer des autres routes de l'application.
"""
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


from api.v1.views.index import *