from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class PDFEditorUI(QMainWindow): #QMainWindow sınıfından türetilen PDFEditorUI sınıfı
    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.

        self.init_ui() # arayüzü içeri aktarma fonksiyonun çağır.

    # arayüzü içeri aktarma fonksiyonu.
    def init_ui(self): loadUi("..\\ui\\editor_ui.ui", self)

    