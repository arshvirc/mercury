from nba_api.stats.endpoints import playercareerstats, commonteamroster, playergamelog
from nba_api.stats.static import players, teams

import pandas as pd


def get_player_id(player_name):
    player_dict = players.find_players_by_full_name(player_name)
    if player_dict:
        return player_dict[0]['id']
    return None

def get_team_logo_url(team_abbreviation):
    # This is a placeholder for team logos. You might need to change the URL or use a different source.
    return f"https://i.cdn.turner.com/nba/nba/assets/logos/teams/primary/web/{team_abbreviation}.svg"

def get_player_season_avg(player_id):
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    stats = career.get_data_frames()[0]
    latest_season = stats[stats['SEASON_ID'] == stats['SEASON_ID'].max()]
    return latest_season.to_dict('records')[0] if not latest_season.empty else None

def get_complete_player_info(player_name):
    player_id = get_player_id(player_name)
    info = {}

    if player_id:
        player_stats = get_player_season_avg(player_id)
        team_name, team_abbreviation = get_team_info(player_stats['TEAM_ID'])


        if team_name and team_abbreviation:
            # team_logo_url = get_team_logo_url(team_abbreviation)

            info['player'] = player_name
            info['team'] = team_name
            info['season_average'] = player_stats
            # info['logo'] = team_logo_url
            return info
        else:
            return { "msg": "Team information not found."}
    else:
        return { "msg": "Player not found."}

# ????

def get_player(id=None):
  player = players.find_player_by_id(id)
  return player

def get_game_logs(id):
  # playoffs = playergamelog.PlayerGameLog(id, season_type_all_star='Playoffs').get_data_frames()[0]
  reg_season = playergamelog.PlayerGameLog(id).get_data_frames()[0]
  # return pd.concat([reg_season, playoffs], ignore_index=True)
  return reg_season

def get_team_roster(id):
  roster = commonteamroster.CommonTeamRoster(id).get_data_frames()[0]
  return roster[["PLAYER", "POSITION", "PLAYER_ID"]]

def retrieve_team_data(id):
  roster = get_team_roster(id)
  player_dict = {}
  for i in roster.index:
    player_id = (roster['PLAYER_ID'][i])
    print(roster['PLAYER'][i])
    p = get_player(str(player_id))
    if p is not None:
      game_logs = get_game_logs(p['id'])
      player_dict[p['full_name']] = game_logs

  return player_dict

def get_teams():
  nba_teams = {}
  for team in teams.get_teams():
    nba_teams[team['full_name']] = {
      'id': team['id'],
      'abbreviation': team['abbreviation']
    }
  return nba_teams

def get_team_data(team_name="Boston Celtics"):
  nba_teams = get_teams()
  team = nba_teams[team_name]
#   team_data = retrieve_team_data(team['id'])
  print(team)
  return team

def get_all_logs(team_name):
    print(f"Getting team data for {team_name}")
    return get_team_data(team_name)


def populate_team_collection():
    nba_teams = {}
    for team in teams.get_teams():
        nba_teams[team['full_name']] = team
    return nba_teams



'''
Here are the Exported Function for the NBA Database Maintenance Code

'''
      
