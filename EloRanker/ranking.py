from basicEloRanker import BasicEloRanker
from percentageRanker import PercentageRanker

class Ranking():
    
    def __init__(self, name, ranked_players = None, 
                 ranked_matches = None, rankers = None):
        self.name = name
        self.id = id(self)
        if not ranked_players:
            self.ranked_players = []
        else:
            self.ranked_players = ranked_players
        if not ranked_matches:
            self.ranked_matches = []
        else:
            self.ranked_matches = ranked_matches
        self.basicEloRanker = BasicEloRanker()
        self.percentageRanker = PercentageRanker()
        if not rankers or not isinstance(rankers, list):
            self.rankers = [self.basicEloRanker, self.percentageRanker]
        
    def addPlayer(self, player):
        for ranker in self.rankers:
            player.rankings[ranker.getRankerName()] = ranker.initRanking()
        self.ranked_players.append(player)
    
    def addMatch(self, match):
        for ranker in self.rankers:
            (w_player, w_player_rank), (l_player, l_player_rank) = ranker.computeRanking(match)
            w_player.rankings[ranker.getRankerName()] = w_player_rank
            l_player.rankings[ranker.getRankerName()] = l_player_rank
        self.ranked_matches.append(match)
                
    def getRankings(self, reverse = True):
        return {ranker.getRankerName() : ranker.sort(self.ranked_players, reverse) for ranker in self.rankers}
    
    def match_prediction(player1, player2):
        pass
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{} : ({}, {}, {})'. \
                format(class_name, self.name, self.ranked_players ,self.rankers)