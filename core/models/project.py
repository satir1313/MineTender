from .pit import Pit
from .assumption import Assumption

class Project:
        
    def __init__(self):
        self.pits = []
        self.path = None
        self.assumption = Assumption()
        
    def add_pit(self, pit):
        self.pits.append(pit)
    
