import pandas as pd
from ranking import Ranking
from player import Player
from match import Match

#Create a new season ranking
ranking = Ranking('season-1')

# Read the player data
player_data = pd.read_csv('data/player_data.csv')
print('---------------- Ranked Players ---------------------')
for index, row in player_data.iterrows():
    name = [elem.strip() for elem in row['name'].split(',')]
    name = name[1] + ' ' + name[0]
    print(name, row['id'], row['club'])
    ranking.addPlayer(Player(name, row['club'], row['id']))
    

# Read the match data
match_data = pd.read_csv('data/match_data.csv')
print('---------------- Ranked Matches ---------------------')
missing_player_names = []
for index, row in match_data.iterrows():
    print(row['home_player'], row['away_player'], row['home_point'], row['away_point'])
    player1 = ranking.find_player_by_name(row['home_player'])
    player2 = ranking.find_player_by_name(row['away_player'])
    if not player1: missing_player_names.append(row['home_player'])
    if not player2: missing_player_names.append(row['away_player'])
    match = Match(player1, player2, row['home_point'], row['away_point'])
    ranking.addMatch(match)
    
print('---------------- Missing Players ---------------------')
print(missing_player_names)

print('-------------------- Rankings -------------------------')
print(ranking.getRankings())