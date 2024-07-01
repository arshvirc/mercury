from nba_api.stats.endpoints import playergamelog

def get_playoff_games(player_id):
  return playergamelog.PlayerGameLog(player_id=player_id, season_type_all_star='Playoffs').get_data_frames()[0].to_dict(orient='records')

def get_regular_games(player_id):
  return playergamelog.PlayerGameLog(player_id=player_id).get_data_frames()[0].to_dict(orient='records')