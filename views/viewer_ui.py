from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.uic import loadUi

class PDFViewerUI(QMainWindow): #QMainWindow sınıfından türetilen PDFReaderUI sınıfı
    def __init__(self, parent = None): 
        super().__init__(parent) # QMainWindow sınıfını başlat.

        self.init_ui() # arayüz dosyasını içeri aktarma fonksiyonunu çağır.
        self.set_widget_properties() # arayüz bileşenlerinin özelliklerini ayarlama fonksiyonunu çağır.

    # arayüz dosyasını içeri aktar.
    def init_ui(self): loadUi('..\\ui\\reader_ui.ui', self)

    # arayüz bileşenlerinin özelliklerini ayarla.
    def set_widget_properties(self): 

        self.browse_file_push_button.clicked.connect(self.browse_file_push_button_clicked) # dosya tarayıcı butonuna tıklandığında browse_file_push_button_clicked fonksiyonunu çağır.
    
        self.next_page_push_button.clicked.connect(self.next_page_push_button_clicked) # sonraki sayfa butonuna tıklandığında next_page_push_button_clicked fonksiyonunu çağır.
    
        self.previous_page_push_button.clicked.connect(self.previous_page_push_button_clicked) # önceki sayfa butonuna tıklandığında previous_page_push_button_clicked fonksiyonunu çağır.

        self.zoom_in_push_button.clicked.connect(self.zoom_in_push_button_clicked) # yakınlaştırma butonuna tıklandığında zoom_in_push_button_clicked fonksiyonunu çağır.

        self.zoom_out_push_button.clicked.connect(self.zoom_out_push_button_clicked) # uzaklaştırma butonuna tıklandığında zoom_out_push_button_clicked fonksiyonunu çağır.

        self.go_to_page_push_button.clicked.connect(self.go_to_page_push_button_clicked) # sayfaya git butonuna tıklandığında go_to_page_push_button_clicked fonksiyonunu çağır.
    

    # dosya tarayıcı butonuna tıklandığında çağrılan fonksiyon.
    def browse_file_push_button_clicked(self):
        selected_file_path, _ = QFileDialog.getOpenFileName(self, "SELECT '.pdf' FILE", "", "PDF Files (*.pdf)")  

        self.log_recent_pdf_file(str(selected_file_path))


    # sonraki sayfa butonuna tıklandığında çağrılan fonksiyon.
    def next_page_push_button_clicked(self): pass 

    # önceki sayfa butonuna tıklandığında çağrılan fonksiyon.
    def previous_page_push_button_clicked(self): pass

    # yakınlaştırma butonuna tıklandığında çağrılan fonksiyon.
    def zoom_in_push_button_clicked(self): pass

    # uzaklaştırma butonuna tıklandığında çağrılan fonksiyon.
    def zoom_out_push_button_clicked(self): pass

    # sayfaya git butonuna tıklandığında çağrılan fonksiyon.
    def go_to_page_push_button_clicked(self): pass 


