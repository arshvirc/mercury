from flask import Blueprint, request, jsonify
from app.firebase.fav import getFavourites, addToFavourites
# from app.firebase.nbaplayers import create_players

fav_bp = Blueprint('fav', __name__)

@fav_bp.route('/favourites/<uid>', methods=['PUT'])
def add_favourites(uid):
    try:
        body = request.get_json()
        addToFavourites(uid, body)
        return jsonify({"Message": "Added to Favourite"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@fav_bp.route('/favourites/<uid>', methods=['GET'])
def get_favourites(uid):
    try:
      favourites = getFavourites(uid)
      return jsonify(favourites), 200
    except Exception as e:
      return jsonify({"error": str(e)}), 500