from flask import Blueprint, request, jsonify
from app.firebase.nbateams import get_teams

info_bp = Blueprint('team', __name__)

@info_bp.route('/teams', methods=['GET'])
def initialize_teams():
    try:
        teams = get_teams()
        return jsonify(teams), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500