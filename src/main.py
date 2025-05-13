import sys
from PyQt5.QtWidgets import QApplication
import os 

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ui'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'recent'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from main_ui import PDFEditorMainUI

class PDFEditorMainApp: # PDFEditorMainApp sınıfı
    def __init__(self): self.init_main_ui()
        

    # uygulama ana pencresini başlat.
    def init_main_ui(self):            
        self.main_app = QApplication(sys.argv)

        self.main_win = PDFEditorMainUI()     
        self.main_win.show()

        self.main_app.exec_()

    # uygulama dosyalarının bütünlüğünü kontrol et.
    def confirm_files(self): print("files confirmed.")

    # uygulamayı kapat.
    def close_app(self): pass         

if __name__ == '__main__':
    pdf_editor_app = PDFEditorMainApp() # PDFEditorMainApp sınıfından bir nesne oluştur.
    pdf_editor_app.confirm_files() # uygulama dosyalarının bütünlüğünü kontrol et.
    
    pdf_editor_app.init_main_ui()
