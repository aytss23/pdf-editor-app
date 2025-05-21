from PyQt5.QtWidgets import QMainWindow

from PyQt5.uic import loadUi

class PDFViewerUI(QMainWindow): #QMainWindow sınıfından türetilen PDFViewerUI sınıfı
    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.

        self.init_ui() # arayüz dosyasını içeri aktarma fonksiyonunu çağır.

    # arayüz dosyasını içeri aktar.
    def init_ui(self): loadUi('views\\resources\\ui\\viewer_ui.ui', self)

    # PDF Dosyasını ekranda görüntüle.
    def display_page_image(self, page_pixmap): self.page_image_display_label.setPixmap(page_pixmap)

    
    #PDF Dosyasının sayfa sayısını ve güncel sayfa değerini göster.
    def update_page_info(self, current_page, max_page):
        self.current_page_line_edit.setText(str(current_page)) # şu an görüntülenen sayfa bilgisini güncelle.

        self.max_page_line_edit.setText(str(max_page)) # PDF dosyasının sayfa sayısını görüntüle.
        
