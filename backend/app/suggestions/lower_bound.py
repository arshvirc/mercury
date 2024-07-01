from .util import relevant_stats, bet365_props, fanduel_props, bet365_props2, fanduel_props2
import app.firebase.nbateams as nbateams
import app.firebase.nbaplayers as nbaplayers
import pandas as pd

def get_team_suggestions(team_name):
  players = nbaplayers.get_players_by_team(team_name)
  suggestions = []
  for player_name in players:
    player = players[player_name]
    if player['season_log'] == []:
      continue
    log = pd.DataFrame(player['season_log'])
    for obj in relevant_stats:
      stat = obj['stat']
      bet365_min = obj['bet365_min']
      fanduel_min = obj['fanduel_min']
      stat_info = {}
      mean = log[stat].mean()
      std = log[stat].std()

      stat_info['player'] = player['PLAYER']
      stat_info['stat'] = stat
      stat_info['mean'] = round(mean, 2)
      stat_info['std']  = round(std, 2)
      stat_info['suggestion'] = mean - std
      stat_info['bet365_prop_milestone'] = bet365_props(round(mean - std, 2), stat)
      stat_info['fanduel_prop_milestone'] = fanduel_props(round(mean - std, 2), stat)

      failed_games = log[stat_info['suggestion'] > log[stat]]
      stat_info['games_started'] =  len(log)
      stat_info['fails'] =  len(failed_games)
      stat_info['failrate'] =  round(len(failed_games)/len(log),2)

      if stat_info['suggestion'] >= bet365_min or stat_info['suggestion'] >= fanduel_min:
        suggestions.append(stat_info)
  return suggestions


def test_team_suggestions(team_name, suggestions):
  team = nbateams.get_team(team_name)
  team_season_games = pd.DataFrame(team['season_log'])[['Game_ID']]
  players = nbaplayers.get_players_by_team(team_name)
  game_logs = team_season_games[['Game_ID']]
  for suggestion in suggestions:
    player_name = suggestion['player']
    player = players[player_name]
    stat = suggestion['stat']
    player_season_games = pd.DataFrame(player['season_log'])[['Game_ID', stat]]
    player_relevant_stat = player_season_games[['Game_ID', stat]]
    player_relevant_stat[f'{stat}_{player_name}'] = player_relevant_stat[stat]
    player_named_logs = player_relevant_stat[['Game_ID', f'{stat}_{player_name}']]
    game_logs = pd.merge(game_logs, player_named_logs, on='Game_ID', how='left')
    
  filtered_df = game_logs
  for suggestion in suggestions:
    player_name = suggestion['player']
    player = players[player_name]
    stat = suggestion['stat']
    bet365_prop_milestone = suggestion['bet365_prop_milestone']
    if bet365_prop_milestone is None:
      bet365_prop_milestone = suggestion['fanduel_prop_milestone']
    filtered_df = filtered_df[(filtered_df[f'{stat}_{player_name}'] >= bet365_prop_milestone) | (pd.isna(filtered_df[f'{stat}_{player_name}']))]

  return filtered_df.to_dict(orient='records')


def test_all_teams():
  teams = nbateams.get_teams()
  results = {}
  for team in teams:
    team_name = team['full_name']
    print(team_name)
    suggestions = get_team_suggestions(team_name)
    successful_games = test_team_suggestions(team_name, suggestions)
    successes = len(successful_games)
    results[team_name] = {
        "wins": successes,
        # "suggestions": suggestions
    }
  return results



def get_rolling_team_suggestions(team_name):
  team = nbateams.get_team(team_name)
  players = nbaplayers.get_players_by_team(team_name)

  team_game_logs = pd.DataFrame(team['season_log'])
  team_game_logs['GAME_DATE'] = pd.to_datetime(team_game_logs['GAME_DATE'], format='%b %d, %Y')
  games = {}
  for idx in range(len(team_game_logs)-2, -1, -1):
    team_game = team_game_logs.iloc[idx]
    game_id = team_game['Game_ID']
    game_date = team_game['GAME_DATE']
    print(f"Row {idx}")
    suggestions = []
    for player_name in players:
      player = players[player_name]
      if player['season_log'] == []: continue

      season_logs = pd.DataFrame(player['season_log'])
      season_logs['GAME_DATE'] = pd.to_datetime(team_game_logs['GAME_DATE'], format='%b %d, %Y')
      previous_games = season_logs[season_logs['GAME_DATE'] < game_date]
      player_game = season_logs[season_logs['Game_ID'] == game_id]
      if len(previous_games) == 0: continue
      print(len(previous_games) )

      for obj in relevant_stats:
        stat = obj['stat']
        bet365_min = obj['bet365_min']
        fanduel_min = obj['fanduel_min']
        stat_info = {}
        mean = previous_games[stat].mean()
        std = previous_games[stat].std()

        stat_info['player'] = player['PLAYER']
        stat_info['stat'] = stat
        stat_info['mean'] = round(mean, 2)
        stat_info['std']  = round(std, 2)
        stat_info['suggestion'] = round(mean - std, 2)
        stat_info['bet365_prop_milestone'] = bet365_props(round(mean - std, 2), stat)
        stat_info['fanduel_prop_milestone'] = fanduel_props(round(mean - std, 2), stat)

      

        if stat_info['suggestion'] >= bet365_min or stat_info['suggestion'] >= fanduel_min:
          stat_info['actual'] = int(player_game[stat].iloc[0])
          if (stat_info['bet365_prop_milestone'] is not None and int(stat_info['bet365_prop_milestone']) <= int(player_game[stat].iloc[0]) ) or (stat_info['fanduel_prop_milestone'] is not None and int(stat_info['fanduel_prop_milestone']) <= int(player_game[stat].iloc[0])):
            stat_info['isSuccess'] = True
          else:
            stat_info['isSuccess'] = False
          suggestions.append(stat_info)

    games[game_id] = suggestions
  return games


def test_rolling_suggestions(team_name, games):
  team = nbateams.get_team(team_name)
  team_season_games = pd.DataFrame(team['season_log'])[['Game_ID']]
  players = nbaplayers.get_players_by_team(team_name)
  game_logs = team_season_games[['Game_ID']]
  ans = 0

  for game in games.keys():
    success = 1
    for suggestion in games[game]:
      if not suggestion['isSuccess']: 
        success = 0
        break;
    ans = ans + success

  return ans