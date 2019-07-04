# Game type constants
GAME_TYPE_STRAIGHT_POOL = '14-1'
GAME_TYPE_8_BALL = '8-Ball'
GAME_TYPE_9_BALL = '9-Ball'
GAME_TYPE_10_BALL = '10-Ball'
GAME_TYPE_DEFAULT = 'default'

# Match outcome constants
OUTCOME_SCORE_WIN = 1.0
OUTCOME_SCORE_LOSS = 0.0
OUTCOME_SCORE_DRAW = 0.5

class Match():
    
    def __init__(self, player1, player2, player1Points,
                 player2Points, gameType = GAME_TYPE_DEFAULT, match_id = None):
        if not match_id:
            self.match_id = id(self)
        else:
            self.match_id = match_id
        self.player1 = player1
        self.player2 = player2
        self.player1Points = player1Points
        self.player2Points = player2Points
        self.gameType = gameType
        
    def winningPlayer(self):
        return self.player1 if self.player1Points > self.player2Points \
                            else self.player2
                            
    def losingPlayer(self):
        return self.player1 if self.player1Points < self.player2Points \
                            else self.player2
                            
    def __repr__(self):
        class_name = type(self).__name__
        return '{} : ({}, {}, {}, {}, {})'. \
                format(class_name, self.player1.name, self.player2.name,
                       self.player1Points, self.player2Points, self.gameType)
                            
                            