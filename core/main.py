import sys
from ui.main_ui.gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from core.helpers import Helper
from PyQt5.QtGui import QValidator, QStandardItemModel
from PyQt5.QtCore import QAbstractTableModel, Qt


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
        self.ui.pushButton.clicked.connect(lambda: self.update_label()) 

        self.ui.btn_equipment_update.clicked.connect(lambda: self.populate_equipment_combobox())

        self.ui.btn_equipment_select.clicked.connect(lambda: self.add_equipment())

    ### validate the input is an integer number between 0 and 100 to represent the percentage
    def validate_percentage_input(self):
        rx  = QtCore.QRegExp('\\b([0-9]|[1-9][0-9]|100)\b.[0-9]')
        val = QtGui.QRegExpValidator(rx)
        return val

    def update_label(self):
        self.ui.label.setText("text has been changed!")

    def populate_equipment_combobox(self):
        items = Helper.read_equipment_excel()
        self.ui.cb_equipment_name.clear()
        if items is None:
            pass
        self.ui.cb_equipment_name.addItems(items)

    def validate_assumptions(self):        
        self.ui.le_duties.setValidator(self.validate_percentage_input())

    def add_equipment(self):
        selected_equipment = self.ui.cb_equipment_name.currentText()
        # to use QTableView see: https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QTableView.html
        # table_model = EquipmentTableViewModel([[selected_equipment,2]])
        # self.ui.tv_equipment.setModel(table_model) 
  

        


def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.populate_equipment_combobox()
    window.validate_assumptions()
    sys.exit(app.exec_())  

if __name__ == "__main__":
   run()