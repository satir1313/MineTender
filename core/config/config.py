from ..models.project import Project

def init():
    global project
    project = Project()
    
if __name__ == "__main__":
    init()