from PyQt5.QtWidgets import QFileDialog
from .models.project import Project
import pickle

class LoadProject():
    def import_project():
        file_name = QFileDialog.getOpenFileName(None, 'open file', 'C:\\')
        return file_name[0]

    def create_project():
        project = Project()
        save_object(project)
        print("A new projct is created")
        
def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

if __name__ == "__main": 
    load = LoadProject()       
    load.create_project()
