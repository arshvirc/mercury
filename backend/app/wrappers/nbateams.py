from nba_api.stats.endpoints import commonteamroster, teamgamelog
from nba_api.stats.static import teams
import time

''' 
get_all_team_data() updates the teams collection with the following data:
  abbreviation: "BOS"
  city: "Boston"
  full_name: "Boston Celtics"
  id: 1610612738
  nickname: "Celtics"
  state: "Massachusetts"
  year_founded: 1946
  roster: [players]
  playoff_log: [games]
  season_log: [games]
'''


def get_teams():
  return teams.get_teams()

def get_playoff_games(team_id):
  return teamgamelog.TeamGameLog(team_id=team_id, season_type_all_star='Playoffs').get_data_frames()[0].to_dict(orient='records')

def get_regular_games(team_id):
  return teamgamelog.TeamGameLog(team_id=team_id).get_data_frames()[0].to_dict(orient='records')

def get_roster(team_id):
  roster = commonteamroster.CommonTeamRoster(team_id=team_id).get_data_frames()[0]
  roster = roster[['PLAYER', 'PLAYER_ID', 'POSITION', 'HOW_ACQUIRED', 'SEASON', 'NUM']]
  return roster.to_dict(orient='records')