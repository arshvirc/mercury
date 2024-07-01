from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import pandas as pd

def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.routes.initialization import initialization_bp
    app.register_blueprint(initialization_bp)

    from app.routes.suggestions import suggestions_bp
    app.register_blueprint(suggestions_bp)

    from app.routes.fav import fav_bp
    app.register_blueprint(fav_bp)

    from app.routes.info import info_bp
    app.register_blueprint(info_bp)

    return app





# DATABASE INITIALIZATION ROUTES
# @app.route('/api/initialize_teams', methods=['GET'])
# def initialize_teams():
#     nba_teams = get_teams()
#     try:
#         for team_name in nba_teams.keys():
#             team_data = nba_teams[team_name]
#             db.collection('Teams').document(team_name).set(team_data)
#             print(f"Added {team_name} with ID {team_name}")
#         return jsonify({"message": "Populated Teams Collection"}), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
# @app.route('/api/initialize_each_team/', methods=['GET'])
# def initialize_each_team():
#     try:
#         teams_ref = db.collection('Teams')
#         docs = teams_ref.stream()
#         team_ids = [doc.id for doc in docs]
#         for team_name in team_ids:
#             print(team_name)
#             team_ref = db.collection('Teams').document(team_name)
#             team = team_ref.get()

#             if team.exists:
#                 team_data = team.to_dict()
#                 team_id = team_data['id']
#                 roster_df = get_team_roster(team_id)
#                 for index, row in roster_df.iterrows():
#                     try:
#                         doc_id = row['PLAYER']  # Assuming 'team_id' is the unique field
#                         player_id = row['PLAYER_ID']
#                         print(f"Attempting to add {doc_id}: {player_id}")
#                         player_data = row.to_dict()
#                         game_log = get_game_logs(player_id)
#                         dict_records = game_log.to_dict(orient='records')
#                         print(dict_records)

#                         player_data['LOGS'] = dict_records
#                         db.collection(team_name).document(doc_id).set(player_data)
#                         print(f"Added {doc_id}")
#                     except Exception as e:
#                         print(f"Error adding team: {e}")
#                     time.sleep(3)
                    
#             time.sleep(20)
#         return jsonify({"Message": f":Completed initializating all teams{team_name}"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # WEB APPLICATION ASPECTS
# @app.route('/api/teams', methods=['GET'])
# def get_teams():
#     teams_ref = get_teams()
#     docs = teams_ref.stream()
#     teams = [doc.to_dict() for doc in docs]
#     return jsonify({"message": teams}), 200



# @app.route('/api/player-info/<name>', methods=['GET'])
# def get_player(name):
#     player_name = name.lower()
#     print(player_name)
#     player_info = get_complete_player_info(player_name)
#     if player_info:
#         return jsonify(player_info)
#     else:
#         return jsonify({'error': 'Player not found'}), 404
    

# def bet365_props(val, stat):
#     milestones = {
#         'PTS': [5, 10, 15, 20, 25, 30, 40, 50, 60],
#         'REB': [3, 5, 7, 9, 11, 13],
#         'AST': [3, 5, 7, 9, 11, 13],
#         'STL': [1, 2, 3, 4, 5, 6],
#         'BLK': [1, 2, 3, 4, 5, 6],
#         'FG3M': [1, 2, 3, 4, 5, 6]
#     }
#     relevant_arr = milestones[stat]
#     index = bisect.bisect_right(relevant_arr, val)
#     return relevant_arr[index - 1] if index > 0 else None

# def fanduel_props(val, stat):
#     milestones = {
#         'PTS': [5, 10, 15, 20, 25, 30, 40, 50, 60],
#         'REB': [4, 6, 8, 10, 12, 14],
#         'AST': [2, 4, 6, 8, 10, 12, 14],
#         'STL': [1, 2, 3, 4, 5, 6],
#         'BLK': [1, 2, 3, 4, 5, 6],
#         'FG3M': [1, 2, 3, 4, 5, 6]
#     }
#     relevant_arr = milestones[stat]
#     index = bisect.bisect_right(relevant_arr, val)
#     return relevant_arr[index - 1] if index > 0 else None


# @app.route('/api/team-suggestions/<team>', methods=['GET'])
# def get_team_suggestions(team):
#     print(team)
#     team_ref = db.collection(team)
#     players = [player.to_dict() for player in team_ref.stream()]

#     relevant_stats = [
#         {'stat': 'PTS', 'bet365_min': 5, 'fanduel_min': 5},
#         {'stat': 'REB', 'bet365_min': 3, 'fanduel_min': 4},
#         {'stat': 'AST', 'bet365_min': 3, 'fanduel_min': 2},
#         {'stat': 'FG3M', 'bet365_min': 1, 'fanduel_min': 1},
#         {'stat': 'BLK', 'bet365_min': 1, 'fanduel_min': 1},
#         {'stat': 'STL', 'bet365_min': 1, 'fanduel_min': 1},
#     ]

#     suggestions = []
#     for player in players:
#         log = pd.DataFrame(player['LOGS'])
#         for obj in relevant_stats:
#             stat = obj['stat']
#             bet365_min = obj['bet365_min']
#             fanduel_min = obj['fanduel_min']
#             stat_info = {}
#             mean = log[stat].mean()
#             std = log[stat].std()

#             stat_info['player'] = player['PLAYER']
#             stat_info['stat'] = stat
#             stat_info['mean'] = round(mean, 2)
#             stat_info['std']  = round(std, 2)
#             stat_info['suggestion'] = round(mean - std, 2)
#             stat_info['bet365_prop_milestone'] = bet365_props(round(mean - std, 2), stat)
#             stat_info['fanduel_prop_milestone'] = fanduel_props(round(mean - std, 2), stat)

#             failed_games = log[stat_info['suggestion'] > log[stat]]
#             stat_info['games_started'] =  len(log)
#             stat_info['fails'] =  len(failed_games)
#             stat_info['failrate'] =  round(len(failed_games)/len(log),2)

#             if stat_info['suggestion'] >= bet365_min or stat_info['suggestion'] >= fanduel_min:
#                 suggestions.append(stat_info)
#                 # suggestions[player['PLAYER']] = player_info
#     response = make_response(jsonify(suggestions), 200)
#     response.headers['Content-Type'] = 'application/json'
#     return response
    

    



# mock = [
#     {
#         "bet365_prop_milestone": 3,
#         "failrate": 0.1,
#         "fails": 8,
#         "fanduel_prop_milestone": None,
#         "games_started": 83,
#         "mean": 6.47,
#         "player": "Al Horford",
#         "stat": "REB",
#         "std": 2.63,
#         "suggestion": 3.84
#     },
#     {
#         "bet365_prop_milestone": 5,
#         "failrate": 0.18,
#         "fails": 16,
#         "fanduel_prop_milestone": 5,
#         "games_started": 91,
#         "mean": 15.51,
#         "player": "Derrick White",
#         "stat": "PTS",
#         "std": 7.39,
#         "suggestion": 8.11
#     },
#     {
#         "bet365_prop_milestone": None,
#         "failrate": 0.11,
#         "fails": 10,
#         "fanduel_prop_milestone": 2,
#         "games_started": 91,
#         "mean": 4.98,
#         "player": "Derrick White",
#         "stat": "AST",
#         "std": 2.3,
#         "suggestion": 2.68
#     },
#     {
#         "bet365_prop_milestone": 15,
#         "failrate": 0.18,
#         "fails": 16,
#         "fanduel_prop_milestone": 15,
#         "games_started": 88,
#         "mean": 23.22,
#         "player": "Jaylen Brown",
#         "stat": "PTS",
#         "std": 7.7,
#         "suggestion": 15.51
#     },
#     {
#         "bet365_prop_milestone": 3,
#         "failrate": 0.22,
#         "fails": 19,
#         "fanduel_prop_milestone": None,
#         "games_started": 88,
#         "mean": 5.59,
#         "player": "Jaylen Brown",
#         "stat": "REB",
#         "std": 2.58,
#         "suggestion": 3.01
#     },
#     {
#         "bet365_prop_milestone": 15,
#         "failrate": 0.16,
#         "fails": 15,
#         "fanduel_prop_milestone": 15,
#         "games_started": 92,
#         "mean": 26.42,
#         "player": "Jayson Tatum",
#         "stat": "PTS",
#         "std": 7.04,
#         "suggestion": 19.39
#     },
#     {
#         "bet365_prop_milestone": 5,
#         "failrate": 0.16,
#         "fails": 15,
#         "fanduel_prop_milestone": 4,
#         "games_started": 92,
#         "mean": 8.45,
#         "player": "Jayson Tatum",
#         "stat": "REB",
#         "std": 2.96,
#         "suggestion": 5.49
#     },
#     {
#         "bet365_prop_milestone": None,
#         "failrate": 0.11,
#         "fails": 10,
#         "fanduel_prop_milestone": 2,
#         "games_started": 92,
#         "mean": 5.13,
#         "player": "Jayson Tatum",
#         "stat": "AST",
#         "std": 2.18,
#         "suggestion": 2.95
#     },
#     {
#         "bet365_prop_milestone": 1,
#         "failrate": 0.17,
#         "fails": 16,
#         "fanduel_prop_milestone": 1,
#         "games_started": 92,
#         "mean": 2.9,
#         "player": "Jayson Tatum",
#         "stat": "FG3M",
#         "std": 1.65,
#         "suggestion": 1.25
#     },
#     {
#         "bet365_prop_milestone": 5,
#         "failrate": 0.18,
#         "fails": 16,
#         "fanduel_prop_milestone": 5,
#         "games_started": 87,
#         "mean": 12.59,
#         "player": "Jrue Holiday",
#         "stat": "PTS",
#         "std": 5.05,
#         "suggestion": 7.54
#     },
#     {
#         "bet365_prop_milestone": 3,
#         "failrate": 0.23,
#         "fails": 20,
#         "fanduel_prop_milestone": None,
#         "games_started": 87,
#         "mean": 5.49,
#         "player": "Jrue Holiday",
#         "stat": "REB",
#         "std": 2.45,
#         "suggestion": 3.05
#     },
#     {
#         "bet365_prop_milestone": None,
#         "failrate": 0.2,
#         "fails": 17,
#         "fanduel_prop_milestone": 2,
#         "games_started": 87,
#         "mean": 4.74,
#         "player": "Jrue Holiday",
#         "stat": "AST",
#         "std": 2.41,
#         "suggestion": 2.32
#     },
#     {
#         "bet365_prop_milestone": 10,
#         "failrate": 0.13,
#         "fails": 8,
#         "fanduel_prop_milestone": 10,
#         "games_started": 63,
#         "mean": 19.46,
#         "player": "Kristaps Porzingis",
#         "stat": "PTS",
#         "std": 6.92,
#         "suggestion": 12.54
#     },
#     {
#         "bet365_prop_milestone": 3,
#         "failrate": 0.22,
#         "fails": 14,
#         "fanduel_prop_milestone": 4,
#         "games_started": 63,
#         "mean": 6.97,
#         "player": "Kristaps Porzingis",
#         "stat": "REB",
#         "std": 2.76,
#         "suggestion": 4.2
#     }
# ]

# # @app.route('/api/parlay-success', methods=['GET'])
# # def get_parlay_success():
# #     team = 'Boston Celtics'
# #     teams_ref = db.collection(team)
# #     for le