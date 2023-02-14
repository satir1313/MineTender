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
        return file_name[0]

    def create_project():
        project = Project()
        save_object(project)
        
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
        
def create_pit(pit_name, bcm, duties, overhead, markup):
    pit = Pit()
    
    pit.set_name(pit_name)
    pit.set_bcm(bcm)
    pit.set_duties(duties)
    pit.set_overhead(overhead)
    pit.set_markup(markup)
    
    config.project.add_pit(pit)
    for p in config.project.pits:
        print(p.name)
    print(type(config.project))
    return pit

if __name__ == "__main": 
    load = LoadProject()       
    load.create_project()
