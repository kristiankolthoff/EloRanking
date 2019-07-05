import ranker
import match as Match

class BasicEloMarginRanker(ranker.Ranker):
    
    def __init__(self, initRank = 1500.0, div_coef = 400, 
                 k1_factor = 32, k2_factor = 32):
        self.initRank = initRank
        self.div_coef = div_coef
        self.k1_factor = k1_factor
        self.k2_factor = k2_factor

    def initRanking(self):
        return self.initRank
    
    def expected_score(self, p1_rank, p2_rank):
        return 1 / (1 + 10**((p1_rank - p2_rank) / self.div_coef))
    
    def rank_update(self, p_rank, exp_score, outcome, margin):
        return p_rank + self.k1_factor * (outcome - exp_score) \
                    + self.k2_factor * margin
    
    def computeRanking(self, match):
        w_player = match.winningPlayer()
        l_player = match.losingPlayer()
        w_player_rank = w_player.rankings[self.getRankerName()]
        l_player_rank = l_player.rankings[self.getRankerName()]
        exp_w_player = self.expected_score(l_player_rank, w_player_rank)
        exp_l_player = self.expected_score(w_player_rank, l_player_rank)
        w_margin = match.score_diff() / match.race_to()
        l_margin = -w_margin
        w_player_rank = self.rank_update(w_player_rank, 
                                    exp_w_player, Match.OUTCOME_SCORE_WIN, w_margin)
        l_player_rank = self.rank_update(l_player_rank, 
                                    exp_l_player, Match.OUTCOME_SCORE_LOSS, l_margin)
        return (w_player, w_player_rank), (l_player, l_player_rank)
    
    def predict_match(self, player1, player):
        pass
    
    def sort(self, players, reverse = True):
        return sorted(players, reverse = reverse, 
                key = lambda player : player.rankings[self.getRankerName()])
    
    def getRankerName(self):
        return 'basic-elo-margin-ranking'
