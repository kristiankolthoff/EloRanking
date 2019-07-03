import abc

class Ranker(abc.ABC):
    
    @abc.abstractmethod
    def initRanking(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def computeRanking(self, match):
        raise NotImplementedError
        
    @abc.abstractmethod
    def predict_match(self, player1, player):
        raise NotImplementedError
        
    @abc.abstractmethod
    def getRankerName(self):
        raise NotImplementedError
        
    @abc.abstractmethod
    def sort(self, reverse = True):
        raise NotImplementedError