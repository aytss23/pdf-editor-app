from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.uic import loadUi
from models.splitter_model import PDFSplitter

class PDFSplitterUI(QMainWindow): #QMainWindow sınıfından türetilen PDFParserUI sınıfı
    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.

        self.init_ui() # arayüzü içeri aktarma fonksiyonunu çağır.

    def init_ui(self): loadUi("views\\resources\\ui\\split_ui.ui", self) #arayüzü içeri aktar.

    def update_progress(self): return None #işlem ilerlemesiyle arayüzü güncelle. 