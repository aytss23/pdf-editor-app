from PyQt5.QtWidgets import QApplication
from views.main_ui import PDFEditorMainUI
from controllers.main_window_controller import MainWindowController
import os 
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'controllers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'views'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))

class PDFEditorMainApp: # PDFEditorMainApp sınıfı
    def __init__(self): self.init_main_ui()
        
    # uygulama ana pencresini başlat.
    def init_main_ui(self):            
        self.main_app = QApplication(sys.argv)

        self.main_win = MainWindowController()     
        
        self.main_app.exec_()
         
if __name__ == '__main__': pdf_editor_app = PDFEditorMainApp()
    
    
    