import ranker
import match as Match

class BasicEloRanker(ranker.Ranker):
    
    def __init__(self, initRank = 1500, div_coef = 400, k_factor = 32):
        self.initRank = initRank
        self.div_coef = div_coef
        self.k_factor = k_factor

    def initRanking(self):
        return self.initRank
    
    def computeRanking(self, match):
        w_player = match.winningPlayer()
        l_player = match.losingPlayer()
        exp_w_player = 1 / (1 + 
            10**((l_player.rankings[self.getRankerName()] - 
                    w_player.rankings[self.getRankerName()]) / self.div_coef))
        exp_l_player = 1 / (1 + 
            10**((w_player.rankings[self.getRankerName()] - 
                    l_player.rankings[self.getRankerName()]) / self.div_coef))
        w_player_rank = w_player.rankings[self.getRankerName()] + \
                        self.k_factor * (Match.OUTCOME_SCORE_WIN - exp_w_player)
        l_player_rank = l_player.rankings[self.getRankerName()] + \
                        self.k_factor * (Match.OUTCOME_SCORE_LOSS - exp_l_player)
        return (w_player, w_player_rank), (l_player, l_player_rank)
    
    def predict_match(self, player1, player):
        pass
    
    def getRankerName(self):
        return 'basic-elo-ranking'
    
    