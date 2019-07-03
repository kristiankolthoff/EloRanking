import ranker

class PercentageRanker(ranker.Ranker):

    def initRanking(self):
        return (0, 0, 0.0)
    
    def computeRanking(self, match):
        w_player = match.winningPlayer()
        l_player = match.losingPlayer()
        w_wins, w_losses, w_perc = w_player.rankings[self.getRankerName()]
        w_wins += 1; w_perc = w_wins / (w_wins + w_losses)
        l_wins, l_losses, l_perc = l_player.rankings[self.getRankerName()]
        l_losses += 1; l_perc = l_wins / (l_wins + l_losses)
        return (w_player, (w_wins, w_losses, w_perc)), (l_player, (l_wins, l_losses, l_perc))
    
    def predict_match(self, player1, player):
        pass
    
    def sort(self, players, reverse = True):
        return sorted(players, reverse = reverse, key = 
            lambda player : (player.rankings[self.getRankerName()][0], player.rankings[self.getRankerName()][2]))
    
    def getRankerName(self):
        return 'percentage-ranking'
    
    