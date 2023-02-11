from PyQt5.QtWidgets import QFileDialog

def import_project():
    file_name = QFileDialog.getOpenFileName(None, 'open file', 'C:\\')
    return file_name[0]