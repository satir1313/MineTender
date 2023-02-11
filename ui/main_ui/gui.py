# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tw_create = QtWidgets.QTabWidget(self.centralwidget)
        self.tw_create.setGeometry(QtCore.QRect(10, 0, 1101, 541))
        self.tw_create.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tw_create.setIconSize(QtCore.QSize(24, 24))
        self.tw_create.setDocumentMode(True)
        self.tw_create.setObjectName("tw_create")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.le_import = QtWidgets.QLineEdit(self.tab)
        self.le_import.setGeometry(QtCore.QRect(150, 40, 301, 31))
        self.le_import.setObjectName("le_import")
        self.lb_import = QtWidgets.QLabel(self.tab)
        self.lb_import.setGeometry(QtCore.QRect(20, 45, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_import.setFont(font)
        self.lb_import.setObjectName("lb_import")
        self.lb_import_2 = QtWidgets.QLabel(self.tab)
        self.lb_import_2.setGeometry(QtCore.QRect(20, 195, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_import_2.setFont(font)
        self.lb_import_2.setObjectName("lb_import_2")
        self.le_create = QtWidgets.QLineEdit(self.tab)
        self.le_create.setGeometry(QtCore.QRect(150, 190, 301, 31))
        self.le_create.setObjectName("le_create")
        self.btn_browse = QtWidgets.QPushButton(self.tab)
        self.btn_browse.setGeometry(QtCore.QRect(150, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_browse.setFont(font)
        self.btn_browse.setObjectName("btn_browse")
        self.btn_import = QtWidgets.QPushButton(self.tab)
        self.btn_import.setGeometry(QtCore.QRect(300, 90, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_import.setFont(font)
        self.btn_import.setObjectName("btn_import")
        self.btn_create = QtWidgets.QPushButton(self.tab)
        self.btn_create.setGeometry(QtCore.QRect(150, 240, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_create.setFont(font)
        self.btn_create.setObjectName("btn_create")
        self.tw_create.addTab(self.tab, "")
        self.tab_assumption = QtWidgets.QWidget()
        self.tab_assumption.setObjectName("tab_assumption")
        self.pushButton = QtWidgets.QPushButton(self.tab_assumption)
        self.pushButton.setGeometry(QtCore.QRect(820, 460, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.tab_assumption)
        self.label.setGeometry(QtCore.QRect(920, 460, 47, 13))
        self.label.setObjectName("label")
        self.lbl_import_duties = QtWidgets.QLabel(self.tab_assumption)
        self.lbl_import_duties.setGeometry(QtCore.QRect(10, 50, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_import_duties.setFont(font)
        self.lbl_import_duties.setObjectName("lbl_import_duties")
        self.lbl_overhead = QtWidgets.QLabel(self.tab_assumption)
        self.lbl_overhead.setGeometry(QtCore.QRect(10, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_overhead.setFont(font)
        self.lbl_overhead.setObjectName("lbl_overhead")
        self.lbl_markup_capital = QtWidgets.QLabel(self.tab_assumption)
        self.lbl_markup_capital.setGeometry(QtCore.QRect(10, 110, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_markup_capital.setFont(font)
        self.lbl_markup_capital.setObjectName("lbl_markup_capital")
        self.le_duties = QtWidgets.QLineEdit(self.tab_assumption)
        self.le_duties.setGeometry(QtCore.QRect(160, 50, 41, 21))
        self.le_duties.setObjectName("le_duties")
        self.le_overhead = QtWidgets.QLineEdit(self.tab_assumption)
        self.le_overhead.setGeometry(QtCore.QRect(160, 80, 41, 21))
        self.le_overhead.setObjectName("le_overhead")
        self.le_markup_capital = QtWidgets.QLineEdit(self.tab_assumption)
        self.le_markup_capital.setGeometry(QtCore.QRect(160, 110, 41, 21))
        self.le_markup_capital.setObjectName("le_markup_capital")
        self.lbl_equipment_name = QtWidgets.QLabel(self.tab_assumption)
        self.lbl_equipment_name.setGeometry(QtCore.QRect(10, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_equipment_name.setFont(font)
        self.lbl_equipment_name.setObjectName("lbl_equipment_name")
        self.cb_equipment_name = QtWidgets.QComboBox(self.tab_assumption)
        self.cb_equipment_name.setGeometry(QtCore.QRect(80, 20, 211, 21))
        self.cb_equipment_name.setEditable(True)
        self.cb_equipment_name.setCurrentText("")
        self.cb_equipment_name.setPlaceholderText("")
        self.cb_equipment_name.setObjectName("cb_equipment_name")
        self.btn_equipment_update = QtWidgets.QPushButton(self.tab_assumption)
        self.btn_equipment_update.setGeometry(QtCore.QRect(300, 20, 75, 23))
        self.btn_equipment_update.setObjectName("btn_equipment_update")
        self.btn_equipment_select = QtWidgets.QPushButton(self.tab_assumption)
        self.btn_equipment_select.setGeometry(QtCore.QRect(390, 20, 75, 23))
        self.btn_equipment_select.setObjectName("btn_equipment_select")
        self.tv_equipment = QtWidgets.QTableView(self.tab_assumption)
        self.tv_equipment.setGeometry(QtCore.QRect(480, 20, 601, 291))
        self.tv_equipment.setGridStyle(QtCore.Qt.SolidLine)
        self.tv_equipment.setObjectName("tv_equipment")
        self.tw_create.addTab(self.tab_assumption, "")
        self.tab_equipment = QtWidgets.QWidget()
        self.tab_equipment.setObjectName("tab_equipment")
        self.cb_equipment_name_2 = QtWidgets.QComboBox(self.tab_equipment)
        self.cb_equipment_name_2.setGeometry(QtCore.QRect(160, 20, 211, 21))
        self.cb_equipment_name_2.setEditable(True)
        self.cb_equipment_name_2.setCurrentText("")
        self.cb_equipment_name_2.setPlaceholderText("")
        self.cb_equipment_name_2.setObjectName("cb_equipment_name_2")
        self.btn_equipment_update_2 = QtWidgets.QPushButton(self.tab_equipment)
        self.btn_equipment_update_2.setGeometry(QtCore.QRect(380, 20, 75, 23))
        self.btn_equipment_update_2.setObjectName("btn_equipment_update_2")
        self.lbl_equipment_name_2 = QtWidgets.QLabel(self.tab_equipment)
        self.lbl_equipment_name_2.setGeometry(QtCore.QRect(10, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_equipment_name_2.setFont(font)
        self.lbl_equipment_name_2.setObjectName("lbl_equipment_name_2")
        self.tw_create.addTab(self.tab_equipment, "")
        self.tab_ga = QtWidgets.QWidget()
        self.tab_ga.setObjectName("tab_ga")
        self.tw_create.addTab(self.tab_ga, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1114, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionClose)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tw_create.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_import.setText(_translate("MainWindow", "Import project"))
        self.lb_import_2.setText(_translate("MainWindow", "Create  project"))
        self.btn_browse.setText(_translate("MainWindow", "Browse"))
        self.btn_import.setText(_translate("MainWindow", "Import"))
        self.btn_create.setText(_translate("MainWindow", "Create"))
        self.tw_create.setTabText(self.tw_create.indexOf(self.tab), _translate("MainWindow", "Project"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "this is the label"))
        self.lbl_import_duties.setText(_translate("MainWindow", "Equipment import duties"))
        self.lbl_overhead.setText(_translate("MainWindow", "Overhead fixed cost"))
        self.lbl_markup_capital.setText(_translate("MainWindow", "Mark up capital cost"))
        self.lbl_equipment_name.setText(_translate("MainWindow", "Equipment "))
        self.btn_equipment_update.setText(_translate("MainWindow", "Update"))
        self.btn_equipment_select.setText(_translate("MainWindow", "Select"))
        self.tw_create.setTabText(self.tw_create.indexOf(self.tab_assumption), _translate("MainWindow", "Assumption"))
        self.btn_equipment_update_2.setText(_translate("MainWindow", "Update"))
        self.lbl_equipment_name_2.setText(_translate("MainWindow", "Equipment "))
        self.tw_create.setTabText(self.tw_create.indexOf(self.tab_equipment), _translate("MainWindow", "Equipment"))
        self.tw_create.setTabText(self.tw_create.indexOf(self.tab_ga), _translate("MainWindow", "G and A"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
