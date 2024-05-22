from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players, teams
import pandas as pd
import joblib
import requests

def get_player_id(player_name):
    player_dict = players.find_players_by_full_name(player_name)
    if player_dict:
        return player_dict[0]['id']
    return None

def get_team_info(team_id):
    team_dict = teams.find_team_name_by_id(team_id)
    if team_dict:
        return team_dict['full_name'], team_dict['abbreviation']
    return None, None

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
