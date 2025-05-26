from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class PDFViewerUI(QMainWindow): #QMainWindow sınıfından türetilen PDFViewerUI sınıfı
    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.

        self.init_ui() # arayüz dosyasını içeri aktarma fonksiyonunu çağır.

    # arayüz dosyasını içeri aktar.
    def init_ui(self): loadUi('views\\resources\\ui\\viewer_ui.ui', self)

    #PDF Dosyasının sayfa sayısını ve güncel sayfa değerini göster.
    def update_page_info(self, current_page, max_page):
        self.current_page_line_edit.setText(str(current_page)) # şu an görüntülenen sayfa bilgisini güncelle.

        self.max_page_line_edit.setText(str(max_page)) # PDF dosyasının sayfa sayısını görüntüle.
        
    def set_screensize(self):
        if self.isFullScreen(): 
            self.showNormal()
            self.show_full_screen_push_button.setText('FULLSCREEN')
        
        else:
            self.showFullScreen()
            self.show_full_screen_push_button.setText('NORMAL')