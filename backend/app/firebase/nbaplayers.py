import pandas as pd
from app.firebase.firebase import db


def get_players_by_team(team_name):
  players_ref = db.collection(team_name)
  players_docs = players_ref.stream()
  players_array = [doc.to_dict() for doc in players_docs]
  players = {}
  for player in players_array:
    players[player['PLAYER']] = player
  return players

def get_player(team_name, player_name):
  player_ref = db.collection(team_name).document(player_name)
  player = player_ref.get()

  if player.exists: 
    return player.to_dict()
  else: 
    return None
  

import app.wrappers.nbaplayers as nbaplayers 
import app.firebase.nbateams as nbateams 
import time

# Create
def create_players():
  teams = nbateams.get_teams()
  for team in teams:
    team_name = team['full_name']
    print(f'Starting to add players for {team_name}')
    roster = team['roster']
    team_abbreviation = team['abbreviation']
    for player in roster:
      player_id = player['PLAYER_ID']
      player_name = player['PLAYER']
      player['playoff_log'] = nbaplayers.get_playoff_games(player_id)
      player_regular_games = nbaplayers.get_regular_games(player_id)
      if player_regular_games == []: continue
      player_df = pd.DataFrame(player_regular_games)
      player_regular_games = player_df[player_df['MATCHUP'].str.contains(f"{team_abbreviation} ")]
      player['season_log'] = player_regular_games.to_dict(orient='records')

      db.collection(team_name).document(player_name).set(player)
      print(f"Added {player_name}")
      time.sleep(2)
    