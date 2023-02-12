from PyQt5.QtWidgets import QFileDialog
from .models.project import Project
import pickle
import os
import shutil

class LoadProject():
    def import_project():
        file_name = QFileDialog.getOpenFileName(None, 'open file', 'C:\\')
        return file_name[0]

    def create_project():
        project = Project()
        save_object(project)
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "All Files(*);;Text Files(*.txt);;Tender Files(*.mtn)", options = options)

        # save file on local disk
        if file_path:
            shutil.copyfile('./data.pickle', file_path + '.mtn')
            print("file created")
        # remove temorary saved project
        if os.path.exists("data.pickle"):
            os.remove("data.pickle")
        else:
            print("The file does not exist") 
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
