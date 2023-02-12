from .pit import Pit
from .assumption import Assumption

class Project:
        
    def __init__(self):
        self.pit = list[Pit]
        self.assumption = Assumption()
        self.pits = []
    ## getters
    def get_project_name(self):
        return self.name
    
    def get_num_of_pits(self):
        return self.num_of_pits
        
    def get_pits(self):
        return self.pits
    
    #setters
    def set_project_name(self, name):
        self.name = name
    
    def set_num_of_pits(self, num):
        self.num_of_pits= num
        
    def set_pits(self, pits):
        self.pits = pits
    
# if __name__ == "__main__":
#     project = Project()