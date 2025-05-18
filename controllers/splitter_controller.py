from views.splitter_ui import PDFSplitterUI
from models.splitter_model import PDFSplitter
from models.main_model import MainModel
from threading import Thread
class SplitterController():
    def __init__(self):

        # UI sınıfından nesne oluştur ve arayüzü göster.
        self.splitter_ui = PDFSplitterUI()
        self.splitter_ui.show()

        self.set_widget_signals() # arayüz bileşenlerinin özelliklerini ayarlama fonksiyonunu çağır.
    
    # arayüz bileşenlerinin özelliklerini ayarla.
    def set_widget_signals(self): 

        self.splitter_ui.browse_pdf_file_push_button.clicked.connect(self.browse_pdf_file_push_button_clicked) # dosya tarayıcı butonuna tıklandığında ilgili fonksiyonu çağır.

        self.splitter_ui.split_pdf_file_push_button.clicked.connect(self.split_pdf_file_push_button_clicked) # dosya parçalama butonu tıklanınca ilgili fonksiyonu çağır.

        self.splitter_ui.set_pdf_file_result_path_push_button.clicked.connect(self.set_pdf_file_result_path_push_button_clicked) # dosya tarayıcı butonu tıklandığında ilgili fonksiyonu çağır.

    # dosya tarayıcı butonuna tıklanınca çağrılan fonksiyon.
    def browse_pdf_file_push_button_clicked(self): self.splitter_ui.pdf_file_path_line_edit.setText(MainModel.start_file_browser(self.splitter_ui, "SELECT A PDF FILE", "PDF Files (*.pdf)")[0])

    # sonuç dosyası yolu tarayıcı butonu tıklanınca çağrılan fonksiyon.
    def set_pdf_file_result_path_push_button_clicked(self): self.splitter_ui.result_pdf_file_path_line_edit.setText(MainModel.start_folder_browser(self.splitter_ui, "SELECT A RESULT FOLDER")) 

    # dosya parçalama butonu tıklanınca çağrılan fonksiyon.
    def split_pdf_file_push_button_clicked(self): 
        
        def start_split_thread():
            pdf_splitter = PDFSplitter() # PDFSplitter sınıfından nesne oluştur.
            
            # Yolu verilen PDF dosyasından belirli sayfaları ayır ve yolu verilen farklı bir dosyaya yaz.
            pdf_splitter.extract_selected_pages_range(self.splitter_ui.pdf_file_path_line_edit.text(), int(self.splitter_ui.start_page_line_edit.text()), int(self.splitter_ui.end_page_line_edit.text()), self.splitter_ui.result_pdf_file_path_line_edit.text()) 

        splitter_thread = Thread(target=start_split_thread)
        splitter_thread.start()        

        # İşlemde kullanılan PDF dosyasını son kullanılan PDF dosyalarına ekle.
        logger = MainModel()
        logger.log_recent_pdf(self.splitter_ui.pdf_file_path_line_edit.text())