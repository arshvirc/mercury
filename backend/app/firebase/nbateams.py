import pandas as pd
from app.firebase.firebase import db

# Get Teams
def get_teams():
  teams_ref = db.collection('Teams')
  teams_docs = teams_ref.stream()
  teams = [doc.to_dict() for doc in teams_docs]
  return teams

def get_team(team_name):
  team_ref = db.collection('Teams').document(team_name)
  team = team_ref.get()

  if team.exists: 
    return team.to_dict()
  else: 
    return None
  

import app.wrappers.nbateams as nbateams 
import time
# Create
def create_teams():
  teams = nbateams.get_teams()
  for team in teams:
    team_name = team['full_name']
    id = team['id']
    team['playoff_log'] = nbateams.get_playoff_games(id)
    time.sleep(2)
    team['season_log'] = nbateams.get_regular_games(id)
    time.sleep(2)
    team['roster'] = nbateams.get_roster(id)
    time.sleep(2)
    db.collection('Teams').document(team_name).set(team)
    print(f"Added {team_name} with ID {team_name}")
    time.sleep(2)



    

