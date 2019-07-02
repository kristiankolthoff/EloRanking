import ranker

class PerformanceRatingEloRanker(ranker.Ranker):
    
    def __init__(self, initRating = 1000, diff = 400):
        self.initRating = initRating
        self.diff = diff

    def initRankings(self, players):
        for player in players:
            player.ranking = self.initRating
        
    def addPlayerToRanking(self, player, ranking):
        player.ranking = self.initRating
    
    def computeRanking(self, match):
        w_player = match.winningPlayer()
        l_player = match.losingPlayer()
        w_player.ranking = l_player.ranking + self.diff
        l_player.ranking = w_player.ranking - self.diff
