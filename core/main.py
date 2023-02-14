import sys
import os
from ui.main_ui.gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from core.helpers import Helper
from PyQt5.QtGui import QValidator, QStandardItemModel
from PyQt5.QtCore import QAbstractTableModel, Qt
from core.project_services import LoadProject, create_pit
from core.db_context import DB_context as db
sys.path.append('../../')
import core.config.config as config

config.init()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Create a table view to add selected equipment
        self.rows = 15
        self.cols = 5
        self.table_model = QStandardItemModel(self.rows, self.cols)
        self.table_model.setHorizontalHeaderLabels(["Name", "Type", "Brand", "Capacity", "consumption"])
        self.ui.tv_equipment.setModel(self.table_model) 

        applicationName = "Tend Mine"
        self.setWindowTitle(applicationName)
        
        if not os.path.exists('.database'):
            os.mkdir('.database')
            
        self.database  = db('.database')
        self.database.create_tables()

        self.ui.btn_equipment_update.clicked.connect(lambda: self.populate_equipment_combobox())

        self.ui.btn_equipment_select.clicked.connect(lambda: self.add_equipment())
        
        self.ui.btn_save.clicked.connect(lambda: self.create_pit())

        self.ui.actionImport.triggered.connect(lambda: self.load_project())
        
        self.ui.actionNew.triggered.connect(lambda: self.create_project())

    ### validate the input is an integer number between 0 and 100 to represent the percentage
    def validate_percentage_input(self):
        rx  = QtCore.QRegExp('\\b([0-9]|[1-9][0-9]|100)\b.[0-9]')
        val = QtGui.QRegExpValidator(rx)
        return val

    def populate_equipment_combobox(self):
        rows = db.get_all(self.database, 'Equipment')
        self.ui.cb_equipment_name.clear()
    
        if rows is None:
            pass
        
        for item in rows:
            self.ui.cb_equipment_name.addItem(f'{item[1]} {item[2]}')
            
        db.close(self.database)

    def validate_assumptions(self):        
        self.ui.le_duties.setValidator(self.validate_percentage_input())

    def add_equipment(self):
        selected_equipment = self.ui.cb_equipment_name.currentText()
        # to use QTableView see: https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QTableView.html
        # table_model = EquipmentTableViewModel([[selected_equipment,2]])
        # self.ui.tv_equipment.setModel(table_model) 
      
    def create_pit(self):
        pit_name = self.ui.le_pit_name.text()
        bcm = self.ui.le_bcm.text()
        duties = self.ui.le_duties.text()
        overhead = self.ui.le_overhead.text()
        markup = self.ui.le_markup_capital.text()
        create_pit(pit_name, bcm, duties, overhead, markup)
    
        
        
    # load existing project
    def load_project(self):
        LoadProject.import_project()
    
    # create a new project
    def create_project(self):
        LoadProject.create_project()
        

def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.populate_equipment_combobox()
    window.validate_assumptions()
    sys.exit(app.exec_())  

if __name__ == "__main__":
   run()