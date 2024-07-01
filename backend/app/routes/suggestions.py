from flask import Blueprint, jsonify, make_response, request
from app.suggestions.lower_bound import test_team_suggestions, get_team_suggestions, test_all_teams, get_rolling_team_suggestions, test_rolling_suggestions

suggestions_bp = Blueprint('suggestions', __name__)

@suggestions_bp.route('/team-suggestions/<team_name>', methods=['GET'])
def get_suggestions(team_name):
    suggestions = get_team_suggestions(team_name)
    response = make_response(jsonify(suggestions), 200)
    response.headers['Content-Type'] = 'application/json'
    return response

@suggestions_bp.route('/team-rolling-suggestions/<team_name>', methods=['GET'])
def get_rolling_suggestions(team_name):
    suggestions = get_rolling_team_suggestions(team_name)
    response = make_response(jsonify(suggestions), 200)
    response.headers['Content-Type'] = 'application/json'
    return response



@suggestions_bp.route('/test-suggestions', methods=['POST'])
def test_suggestions():
    body = request.get_json()
    suggestions = body['suggestions']
    team_name = body['team_name']
    successful_logs = test_team_suggestions(team_name, suggestions)
    
    return jsonify({"message": "JSON received", "data": successful_logs})


@suggestions_bp.route('/test-team/<team_name>', methods=['GET'])
def test_team(team_name):
    suggestions = get_team_suggestions(team_name)
    successful_logs = test_team_suggestions(team_name, suggestions)
    successes = len(successful_logs)
    
    return jsonify({"message": "JSON received", "data": successes})

@suggestions_bp.route('/test-rolling-team/<team_name>', methods=['GET'])
def test_rolling_team(team_name):
    suggestions = get_rolling_team_suggestions(team_name)
    successes = test_rolling_suggestions(team_name, suggestions)
    
    return jsonify({"message": "JSON received", "data": successes})

@suggestions_bp.route('/test-teams', methods=['GET'])
def test_teams():
    results = test_all_teams()
    return jsonify({"message": "JSON received", "data": results})