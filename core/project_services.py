from PyQt5.QtWidgets import QFileDialog
from .models.project import Project, Pit
import pickle
import os
import shutil
import sys
sys.path.append('../../')
import core.config.config as config

class LoadProject():
    def import_project():
        file_name = QFileDialog.getOpenFileName(None, 'open file', 'C:\\')
        config.project = load_object(filename=file_name[0])

    def create_project():
        save_object(config.project)
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "Tender Files(*.mtn)", options = options)
        
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

def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)
 
 
def create_pit(pit_name, bcm, duties, overhead, markup):
    pit = Pit()
    
    pit.name = pit_name
    pit.bcm = bcm
    pit.duties = duties
    pit.overhead = overhead
    pit.markup = markup
    
    config.project.add_pit(pit)
    for p in config.project.pits:
        print(p.name)
    print(type(config.project))
    return pit

if __name__ == "__main": 
    create_pit()
