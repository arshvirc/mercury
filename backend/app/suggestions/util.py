import bisect

relevant_stats = [
  {'stat': 'PTS', 'bet365_min': 5, 'fanduel_min': 5},
  {'stat': 'REB', 'bet365_min': 3, 'fanduel_min': 4},
  {'stat': 'AST', 'bet365_min': 3, 'fanduel_min': 2},
  {'stat': 'FG3M', 'bet365_min': 1, 'fanduel_min': 1},
  {'stat': 'BLK', 'bet365_min': 1, 'fanduel_min': 1},
  {'stat': 'STL', 'bet365_min': 1, 'fanduel_min': 1},
]


def bet365_props(val, stat):
  milestones = {
    'PTS': [5, 10, 15, 20, 25, 30, 40, 50, 60],
    'REB': [3, 5, 7, 9, 11, 13],
    'AST': [3, 5, 7, 9, 11, 13],
    'STL': [1, 2, 3, 4, 5, 6],
    'BLK': [1, 2, 3, 4, 5, 6],
    'FG3M': [1, 2, 3, 4, 5, 6]
  }
  relevant_arr = milestones[stat]
  index = bisect.bisect_right(relevant_arr, val)
  return relevant_arr[index - 1] if index > 0 else None

def bet365_props2(val, stat):
  milestones = {
    'PTS': [5, 10, 15, 20, 25, 30, 40, 50, 60],
    'REB': [3, 5, 7, 9, 11, 13],
    'AST': [3, 5, 7, 9, 11, 13],
    'STL': [1, 2, 3, 4, 5, 6],
    'BLK': [1, 2, 3, 4, 5, 6],
    'FG3M': [1, 2, 3, 4, 5, 6]
  }
  relevant_arr = milestones[stat]
  index = bisect.bisect_right(relevant_arr, val)
  return relevant_arr[index - 2] if index > 1 else None

def fanduel_props(val, stat):
  milestones = {
    'PTS': [5, 10, 15, 20, 25, 30, 40, 50, 60],
    'REB': [4, 6, 8, 10, 12, 14],
    'AST': [2, 4, 6, 8, 10, 12, 14],
    'STL': [1, 2, 3, 4, 5, 6],
    'BLK': [1, 2, 3, 4, 5, 6],
    'FG3M': [1, 2, 3, 4, 5, 6]
  }
  relevant_arr = milestones[stat]
  index = bisect.bisect_right(relevant_arr, val)
  return relevant_arr[index - 1] if index > 0 else None

def fanduel_props2(val, stat):
  milestones = {
    'PTS': [5, 10, 15, 20, 25, 30, 40, 50, 60],
    'REB': [4, 6, 8, 10, 12, 14],
    'AST': [2, 4, 6, 8, 10, 12, 14],
    'STL': [1, 2, 3, 4, 5, 6],
    'BLK': [1, 2, 3, 4, 5, 6],
    'FG3M': [1, 2, 3, 4, 5, 6]
  }
  relevant_arr = milestones[stat]
  index = bisect.bisect_right(relevant_arr, val)
  return relevant_arr[index - 2] if index > 0 else None