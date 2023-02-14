from .pit import Pit
from .assumption import Assumption

class Project:
        
    def __init__(self):
        self.pits = []
        self.assumption = Assumption()

    ## getters
    def get_project_name(self):
        return self.name
        
    def get_pits(self):
        return self.pits
    
    #setters
    def set_project_name(self, name):
        self.name = name
        
    def add_pit(self, pit):
        self.pits.append(pit)
    
# if __name__ == "__main__":
#     project = Project()