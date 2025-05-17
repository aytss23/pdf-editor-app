from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.uic import loadUi

class PDFSplitterUI(QMainWindow): #QMainWindow sınıfından türetilen PDFParserUI sınıfı
    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.

        self.init_ui() # arayüzü içeri aktarma fonksiyonunu çağır.

        self.set_widget_properties() # arayüz bileşenlerinin özelliklerini ayarlama fonksiyonunu çağır.

    def init_ui(self): loadUi("..\\ui\\split_ui.ui", self) #arayüzü içeri aktar.

    # arayüz bileşenlerinin özelliklerini ayarla.
    def set_widget_properties(self): 

        self.browse_pdf_file_push_button.clicked.connect(self.browse_pdf_file_push_button_clicked) # dosya tarayıcı butonuna tıklandığında ilgili fonksiyonu çağır.

        self.split_pdf_file_push_button.clicked.connect(self.split_pdf_file_push_button_clicked) # dosya parçalama butonu tıklanınca ilgili fonksiyonu çağır.

        self.set_pdf_file_result_path_push_button.clicked.connect(self.set_pdf_file_result_path_push_button_clicked) # dosya tarayıcı butonu tıklandığında ilgili fonksiyonu çağır.

    # dosya tarayıcı butonuna tıklanınca çağrılan fonksiyon.
    def browse_pdf_file_push_button_clicked(self): self.pdf_file_path_line_edit.setText(QFileDialog.getOpenFileName(self, "SELECT '.pdf' FILE", "", "PDF Files (*.pdf)")[0])

    # sonuç dosyası yolu tarayıcı butonu tıklanınca çağrılan fonksiyon.
    def set_pdf_file_result_path_push_button_clicked(self): self.result_pdf_file_path_line_edit.setText(QFileDialog.getExistingDirectory(self, "SELECT RESULT FOLDER") + "/split_pdf_file_result.pdf") 

    # dosya parçalama butonu tıklanınca çağrılan fonksiyon.
    def split_pdf_file_push_button_clicked(self): 
        pdf_splitter = PDFSplitter() # PDFSplitter sınıfından nesne oluştur.

        # Yolu verilen PDF dosyasından belirli sayfaları ayır ve yolu verilen farklı bir dosyaya yaz.
        pdf_splitter.extract_selected_pages_range(self.pdf_file_path_line_edit.text(), int(self.start_page_line_edit.text()), int(self.end_page_line_edit.text()), self.result_pdf_file_path_line_edit.text()) 

        self.log_recent_pdf_file(self.result_pdf_file_path_line_edit.text()) # son kullanulan PDF dosyasını veritabanına kaydet. 

    # son kullanılan PDF Dosyasını veritabanına kaydet.
    def log_recent_pdf_file(self, recent_pdf_file_path): 
        database_manager = RecentPDFDatabaseManager()

        database_manager.log_recent_pdfs(recent_pdf_file_path)

        database_manager.close_database()
