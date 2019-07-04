class Player():
    
    def __init__(self, name, club = None, p_id = None):
        self.name = name
        self.club = club
        if not p_id:
            self.p_id = id(self)
        else:
            self.p_id = p_id
        self.rankings = {}
        
    def __repr__(self):
        class_name = type(self).__name__
        return '{} : ({}, {}, {}, ranking : {})'. \
                format(class_name, self.name, self.club, self.p_id, self.rankings)