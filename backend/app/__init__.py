from flask import Flask, jsonify, request
from flask_cors import CORS
from app.nba_data import get_complete_player_info
from app.models.model1 import predict

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})


@app.route('/api/player-info/<name>', methods=['GET'])
def get_player(name):
    player_name = name.lower()
    print(player_name)
    player_info = get_complete_player_info(player_name)
    if player_info:
        return jsonify(player_info)
    else:
        return jsonify({'error': 'Player not found'}), 404
    
@app.route('/api/player-prediction/<name>', methods=['GET'])
def get_player_prediction(name):
    player_name = name.lower()
    # print(player_name)
    answer = predict()
    print(answer)
    if answer:
        return jsonify({'prediction': answer})
    else:
        return jsonify({'error': 'Player not found'}), 404