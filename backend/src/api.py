import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

db_drop_and_create_all()

# ROUTES


@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.order_by(Drink.id).all()
    return jsonify({
        "success": True,
        "drinks": [drink.short() for drink in drinks]
    })


@app.route('/drinks-detail')
@requires_auth("GET:drinks-detail")
def get_detailed_drinks(jwt):
    drinks = Drink.query.order_by(Drink.id).all()
    return jsonify({
        "success": True,
        "drinks": [drink.long() for drink in drinks]
    })


@app.route('/drinks', methods=["POST"])
@requires_auth("POST:drinks")
def post_drinks(jwt):
    data = request.get_json()
    drink = Drink(title=data['title'], recipe=json.dumps(data['recipe']))
    drink.insert()
    drinks = Drink.query.order_by(Drink.id).all()
    return jsonify({
        "success": True,
        "drinks": [drink.long() for drink in drinks]
    })


@app.route('/drinks/<int:drink_id>', methods=["PATCH"])
@requires_auth("PATCH:drinks")
def update_drinks(jwt, drink_id):
    drink = Drink.query.filter(Drink.id == drink_id).one_or_none()
    if not drink:
        abort(404)
    data = request.get_json()
    if 'title' in data:
        setattr(drink, 'title', data['title'])
    if 'recipe' in data:
        setattr(drink, 'recipe', json.dumps(data['recipe']))
    drink.update()
    return jsonify({
        "success": True,
        "drinks": Drink.query.filter(Drink.id == drink_id).one_or_none().long()
    })


@app.route('/drinks/<int:drink_id>', methods=["DELETE"])
@requires_auth("DELETE:drinks")
def delete_drinks(jwt, drink_id):
    drink = Drink.query.filter(Drink.id == drink_id).one_or_none()
    if not drink:
        abort(404)
    drink.delete()
    return jsonify({
        "success": True,
        "delete": drink_id
    })


# Error Handling

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def Notfound(error):
    return jsonify({
        "success": True,
        "error": 404,
        "description": "Resource not found"
    }), 404


@app.errorhandler(AuthError)
def autherror(error):
    return jsonify({
        "success": True,
        "error": error.status_code,
        "description": error.error["description"]
    }), error.status_code
