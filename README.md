# EloRanking

This project aims to provide some simple [Elo ranking](https://en.wikipedia.org/wiki/Elo_rating_system) implementations that 
can be used to compute meaningful rankings for players in a sports league. Comparing the Elo ratings of two players, we can 
make predictions of the outcome of the match between them. After some matches have been played, the rankings of the corresponding 
players are adapted in order to better reflect and converge to the real rankings and self-correct them. This system is applied in many
games and can e.g. be used for improved matchmaking. Many adaptions of this ranking system exist varying in the computation of the ranking itself and the updating policy of the ranking.

# Example

In order to use the Elo ranking implementation in Python, we first import the ``Ranking``, ``Player`` and ``Match`` classes
and create a new ranking instance.

 ```python
import pandas as pd
from ranking import Ranking
from player import Player
from match import Match

#Create a new season ranking
ranking = Ranking('season-1')
```

Afterwards, we need to add all the players we want to include in the ranking to the ``Ranking`` instance.
In our case, we read the data from a Pandas Dataframe instance.

 ```python
# Read the player data
player_data = pd.read_csv('data/input/player_data.csv')
for index, row in player_data.iterrows():
    name = [elem.strip() for elem in row['name'].split(',')]
    name = name[1] + ' ' + name[0]
    print(name, row['id'], row['club'])
    ranking.addPlayer(Player(name, row['club'], row['id']))
 ```
 
 Now we can add all the matches we observed already. Newly arriving matches can be simply added later and
 the rankings are updated afterwards. As an update policy, we simply recompute the rankings after each individual game. 
 Again, we read the matches from a Pandas Dataframe instance into our ranking.

 ```python
# Read the match data
match_data = pd.read_csv('data/input/match_data.csv')
for index, row in match_data.iterrows():
    print(row['home_player'], row['away_player'], row['home_point'], row['away_point'])
    player1 = ranking.find_player_by_name(row['home_player'])
    player2 = ranking.find_player_by_name(row['away_player'])
    match = Match(player1, player2, row['home_point'], row['away_point'])
    ranking.addMatch(match)
 ```

Finally we can retrieve the different rankings that are currently available.

 ```python
# Retrieve the simple percentage rankings
ranking.printRankingsByName('percentage-ranking')
df_ranking_percentage = ranking.getRankingsByNameAsDataframe('percentage-ranking')
df_ranking_percentage.to_csv('data/rankings/percentage-ranking.csv')

# Retrieve the basic Elo rankings
ranking.printRankingsByName('basic-elo-ranking')
df_ranking_elo = ranking.getRankingsByNameAsDataframe('basic-elo-ranking')
df_ranking_elo.to_csv('data/rankings/basic-elo-ranking.csv')

# Retrieve the Elo margin rankings
ranking.printRankingsByName('basic-elo-margin-ranking')
df_ranking_elo_margin = ranking.getRankingsByNameAsDataframe('basic-elo-margin-ranking')
df_ranking_elo_margin.to_csv('data/rankings/basic-elo-margin-ranking.csv')
```
