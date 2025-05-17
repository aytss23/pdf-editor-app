from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.uic import loadUi 

class PDFConverterUI(QMainWindow): #QMainWindow sınıfından türetilen PDFConverterUI sınıfı
    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.

        self.init_ui() #arayüz dosyasını içeri aktar. 

        self.set_widget_properties() # arayüz bileşenlerinin özelliklerini ayarlayan fonksiyonu çağır.

    # arayüz dosyasını içeri aktaran fonksiyon.
    def init_ui(self): loadUi("..\\ui\\convert_ui.ui", self)

