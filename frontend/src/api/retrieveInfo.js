import apiClient from './apiClient';

const player_data = {
  "name": "shai gilgeous-alexander",
  "season_totals": { 
    "AST": 465,
    "BLK": 67,
    "DREB": 350,
    "FG3A": 269,
    "FG3M": 95,
    "FG3_PCT": 0.353,
    "FGA": 1487,
    "FGM": 796,
    "FG_PCT": 0.535,
    "FTA": 649,
    "FTM": 567,
    "FT_PCT": 0.874,
    "GP": 75,
    "GS": 75,
    "LEAGUE_ID": "00",
    "MIN": 2553,
    "OREB": 65,
    "PF": 184,
    "PLAYER_AGE": 25,
    "PLAYER_ID": 1628983,
    "PTS": 2254,
    "REB": 415,
    "SEASON_ID": "2023-24",
    "STL": 150,
    "TEAM_ABBREVIATION": "OKC",
    "TEAM_ID": 1610612760,
    "TOV": 162
  },
  "team": "Oklahoma City Thunder"
}

export const retrieveInfo = async (name) => {
  try {
    // const response = await apiClient.get(`/api/player-info/${name}`);
    // return response.data;
    return player_data
  } catch (error) {
    console.error('Error fetching data from Info Endpoint:', error);
    throw error;
  }
};