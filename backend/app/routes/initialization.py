from flask import Blueprint, request, jsonify
from app.firebase.nbateams import create_teams
from app.firebase.nbaplayers import create_players

initialization_bp = Blueprint('initialization', __name__)

@initialization_bp.route('/initialization/teams', methods=['GET'])
def initialize_teams():
    try:
        create_teams()
        return jsonify({"Message": "All teams have been initialized"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@initialization_bp.route('/initialization/players', methods=['GET'])
def initialize_players():
    try:
        create_players()
        return jsonify({"Message": "All players have been initialized"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500