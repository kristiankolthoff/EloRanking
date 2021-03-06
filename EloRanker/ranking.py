from basicEloRanker import BasicEloRanker
from basicEloMarginRanker import BasicEloMarginRanker
from percentageRanker import PercentageRanker
import pandas as pd

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
        self.basicEloMarginRanker = BasicEloMarginRanker()
        self.percentageRanker = PercentageRanker()
        if not rankers or not isinstance(rankers, list):
            self.rankers = [self.basicEloRanker, self.basicEloMarginRanker, 
                            self.percentageRanker]
        
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
    
    def getRankingsByName(self, ranker_name, reverse = True):
        for ranker in self.rankers:
            if ranker.getRankerName() == ranker_name:
                return ranker.sort(self.ranked_players, reverse)
        return None
    
    def player_w_ranking_to_dict(self, player, rank, ranker_name):
        return {'rank' : (rank+1), 'name' : player.name, 'club' : player.club, 
                'id' : player.p_id, ranker_name : player.rankings[ranker_name]}
    
    def getRankingsByNameAsDataframe(self, ranker_name, reverse = True):
        for ranker in self.rankers:
            if ranker.getRankerName() == ranker_name:
                ranking = ranker.sort(self.ranked_players, reverse)
                return pd.DataFrame([self.player_w_ranking_to_dict(player, 
                                     index, ranker_name)
                                     for index, player in enumerate(ranking)])
    
    def printRankingsByName(self, ranker_name, reverse = True):
        for ranker in self.rankers:
            if ranker.getRankerName() == ranker_name:
                ranking = ranker.sort(self.ranked_players, reverse)
                for index, player in enumerate(ranking):
                    print('[{}] : ({}, {}, {}   | {})'. \
                format(str((index+1)).zfill(2) , player.name, player.club,
                       player.p_id, player.rankings[ranker.getRankerName()]))
    
    def match_prediction(self, player1, player2):
        pass
    
    def find_player_by_name(self, name):
        for player in self.ranked_players:
            if player.name == name:
                return player
        return None
    
    def __repr__(self):
        class_name = type(self).__name__
        return '{} : ({}, {}, {})'. \
                format(class_name, self.name, self.ranked_players ,self.rankers)