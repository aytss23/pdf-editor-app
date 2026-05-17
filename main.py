import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.win import Ui_MainWindow
from contrl.appctrl import AppController
from core.eng import RenderEngine

class PDFEditorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.controller = AppController(self.ui, None)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = PDFEditorApp()
        
    win.show()
    sys.exit(app.exec_())