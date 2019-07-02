from ranking import Ranking
from match import Match
import ranker
from player import Player

player1 = Player('Player1')
player2 = Player('Player2')
player3 = Player('Player3')
player4 = Player('Player4')


match1 = Match(player1, player2, 6, 7)

ranking = Ranking('season1')
ranking.addPlayer(player1)
ranking.addPlayer(player2)
ranking.addPlayer(player3)
ranking.addPlayer(player4)

ranking.addMatch(match1)

print(ranking.getRankings())