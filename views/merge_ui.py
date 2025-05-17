from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.uic import loadUi 

class PDFMergerUI(QMainWindow): #QMainWindow sınıfından türetilen PDFMergerUI sınıfı
    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.

        self.init_ui() # arayüzü içeri aktarma fonksiyonun çağır.

    # arayüzü içeri aktarma fonksiyonu
    def init_ui(self): loadUi('views\\resources\\ui\\merge_ui.ui', self)

