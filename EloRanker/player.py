class Player():
    
    def __init__(self, name, p_id = None):
        self.name = name
        if not p_id:
            self.p_id = id(self)
        else:
            self.p_id = p_id
        self.rankings = {}
        
    def __repr__(self):
        class_name = type(self).__name__
        return '{} : ({}, {}, ranking : {})'. \
                format(class_name, self.name, self.p_id, self.rankings)