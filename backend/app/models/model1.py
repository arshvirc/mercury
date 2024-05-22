import numpy as np
import pandas as pd
from nba_api.stats.endpoints import playercareerstats, LeagueSeasonMatchups
from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster
from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog, BoxScoreAdvancedV3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib


def get_all_nba_teams():
  nba_teams = {}
  for team in teams.get_teams():
    nba_teams[team['full_name']] = {
      'id': team['id'],
      'abbreviation': team['abbreviation']
    }
  return nba_teams

def get_team_roster(id):
  roster = commonteamroster.CommonTeamRoster(id).get_data_frames()[0]
  return roster[["PLAYER", "POSITION", "PLAYER_ID"]]

def get_player(id=None):
  player = players.find_player_by_id(id)
  return player

def get_game_logs(id):
  # playoffs = playergamelog.PlayerGameLog(id, season_type_all_star='Playoffs').get_data_frames()[0]
  reg_season = playergamelog.PlayerGameLog(id).get_data_frames()[0]
  return reg_season
  # return playoffs
  # return reg_season[["Game_ID", "MATCHUP", "MIN", "WL", "PTS", "REB", "AST", "FG3M", "STL", "BLK", "TOV"]]

def retrieve_team_data(id):
  roster = get_team_roster(id)
  player_dict = {}
  for i in roster.index:
    player_id = (roster['PLAYER_ID'][i])
    p = get_player(str(player_id))
    if p is not None:
      game_logs = get_game_logs(p['id'])
      player_dict[p['full_name']] = game_logs

  return player_dict

interested_players = {
    'Oklahoma City Thunder': ['Shai Gilgeous-Alexander', 'Chet Holmgren'],
}

def get_team_data(team_name="Boston Celtics"):
  nba_teams = get_all_nba_teams()
  team = nba_teams[team_name]
  team_data = retrieve_team_data(team['id'])
  return team_data

def get_player_df(team_data, player_name="Jaylen Brown"):
  game_logs = team_data[player_name]
  dataset = None
  for i in range(game_logs.shape[0]):
    relevant_logs = game_logs.iloc[i+1:][["MIN", "PTS", "REB", "AST", "FG3M", "STL", "BLK", "TOV"]]
    season_avgs = relevant_logs.mean()

    seasons_row = pd.DataFrame(season_avgs).T
    seasons_row = seasons_row.rename(columns={col: col + '_Season' for col in seasons_row.columns})

    last_5_games = relevant_logs.head(5)
    last_5_avgs = last_5_games.mean()

    recent_row = pd.DataFrame(last_5_avgs).T
    recent_row = recent_row.rename(columns={col: col + '_Recent' for col in recent_row.columns})

    values = game_logs.iloc[i][["PTS"]]
    values_df = pd.DataFrame(values).T
    values_df.reset_index(drop=True, inplace=True)

    df_temp = pd.concat([values_df, seasons_row], axis=1)
    df_horizontal = pd.concat([df_temp, recent_row], axis=1)


    if dataset is None :
      dataset = df_horizontal
    else:
      dataset = pd.concat([dataset, df_horizontal], axis=0)

  dataset.reset_index(drop=True, inplace=True)

  return dataset.head(game_logs.shape[0]-1)

interested_players = {
    'Boston Celtics': ['Jayson Tatum'],
    # 'Chicago Bulls': ['DeMar DeRozan', 'Nikola Vucevic'],
    # 'Utah Jazz': ['Collin Sexton', 'Keyonte George', 'Taylor Hendricks', 'Kris Dunn'],
    # 'Houston Rockets': ['Jalen Green', 'Fred VanVleet', 'Jabari Smith Jr', 'Amen Thompson', 'Dillion Brooks'],
    # 'Oklahoma City Thunder': ['Shai Gilgeous-Alexander'],
}

def get_team_logs(teams):
  for team_name in teams:
    team_data = get_team_data(team_name)
    for player_name, game_log in team_data.items():
      names = interested_players[team_name]
      if player_name in names:
        df = get_player_df(team_data, player_name)
        return df

def get_all_logs(teams):
  for team_name in teams:
    team_data = get_team_data(team_name)
    for player_name, game_log in team_data.items():
      names = interested_players[team_name]
      if player_name in names:
        return team_data[player_name]

# Data Sanization

# Preprocess for milestones

# Feature engineering pts/rebound

# Rolling Season Average
# 50 LAST 49 GAMES
# Rolling Last 5 Games Average
# Matchup History All Time

# same shit but standard deviation

# Milestone

crazyset = get_all_logs(['Boston Celtics'])

# Importing necessary libraries



def train_model():
  data = get_team_logs(['Boston Celtics'])
  X = data.drop(columns=['PTS'])
  y = data['PTS']

  # Splitting the data into training and testing sets
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  # Creating and training the linear regression model
  model = LinearRegression()
  model.fit(X_train, y_train)

  # Making predictions on the testing set
  y_pred = model.predict(X_test)

  # Evaluating the model
  mse = mean_absolute_error(y_test, y_pred)
  # print("Mean Absolute Error:", mse)

  # # Printing the coefficients of the model
  # print("Coefficients:", model.coef_)
  # print("Intercept:", model.intercept_)
  return model


def predict():
  model = train_model()
  crazyset = get_all_logs(['Boston Celtics'])
  df = crazyset[["MIN", "PTS", "REB", "AST", "FG3M", "STL", "BLK", "TOV"]]
  season_avgs = df.mean()
  seasons_row = pd.DataFrame(season_avgs).T
  seasons_row = seasons_row.rename(columns={col: col + '_Season' for col in seasons_row.columns})

  last_5_games = df.head(5)
  last_5_avgs = last_5_games.mean()

  recent_row = pd.DataFrame(last_5_avgs).T
  recent_row = recent_row.rename(columns={col: col + '_Recent' for col in recent_row.columns})

  values = df.iloc[0][["PTS"]]
  values_df = pd.DataFrame(values).T
  values_df.reset_index(drop=True, inplace=True)

  df_temp = pd.concat([values_df, seasons_row], axis=1)
  df_horizontal = pd.concat([df_temp, recent_row], axis=1)

  X_real = df_horizontal.drop(columns=['PTS'])
  # print(X_real)

  y_pred = model.predict(X_real)
  return(y_pred)