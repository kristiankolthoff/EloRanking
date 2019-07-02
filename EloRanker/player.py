class Player():
    
    def __init__(self, name):
        self.name = name
        self.id = id(self)
        self.rankings = {}
        self.wins = 0
        self.losses = 0
        
    def __repr__(self):
        class_name = type(self).__name__
        return '{} : ({}, {}, wins : {}, losses : {}, ranking : {})'. \
                format(class_name, self.name, self.id ,self.wins, self.losses, self.rankings)