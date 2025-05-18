from views.merge_ui import PDFMergerUI
from models.main_model import MainModel
from models.merger_model import PDFMerger

class MergerController():
    def __init__(self):

        self.merger_ui = PDFMergerUI() # UI sınıfından nesne türet ve arayüzü oluştur.
        self.merger_ui.show() # arayüzü göster.

        self.set_widget_signals() # arayüz bileşenlerinin özelliklerini ayarlama fonksiyonunu çağır.

        # arayüz bileşenlerinin özelliklerini ayarla.
    def set_widget_signals(self):

        self.merger_ui.browse_pdf_file_a_push_button.clicked.connect(self.browse_pdf_file_a_push_button_clicked) # PDF dosyası A butonuna tıklandığında browse_pdf_file_a_push_button_clicked fonksiyonunu çağır.

        self.merger_ui.browse_pdf_file_b_push_button.clicked.connect(self.browse_pdf_file_b_push_button_clicked) # PDF dosyası B butonuna tıklandığında browse_pdf_file_b_push_button_clicked fonksiyonunu çağır.

        self.merger_ui.merge_pdfs_push_button.clicked.connect(self.merge_pdfs_push_button_clicked) # PDF dosyalarını birleştir butonuna tıklandığında merge_pdf_push_button_clicked fonksiyonunu çağır.

        self.merger_ui.set_pdf_result_path_push_button.clicked.connect(self.set_pdf_result_path_clicked)
    
    # dosya tarayıcı A butonuna tıklandığında çağrılan fonksiyon.
    def browse_pdf_file_a_push_button_clicked(self): self.merger_ui.pdf_file_a_path_line_edit.setText(MainModel.start_file_browser(self.merger_ui, "SELECT FIRST FILE","PDF Files (*.pdf)")[0]) 

    # dosya tarayıcı B butonuna tıklandığında çağrılan fonksiyon.
    def browse_pdf_file_b_push_button_clicked(self): self.merger_ui.pdf_file_b_path_line_edit.setText(MainModel.start_file_browser(self.merger_ui, "SELECT SECOND FILE", "PDF Files (*.pdf)")[0])

    # pdf birleştirme butonuna tıklandığında çağrılan fonksiyon.
    def merge_pdfs_push_button_clicked(self): 
        pdf_merge_manager = PDFMerger()

        pdf_merge_manager.merger_two_pdfs([self.merger_ui.pdf_file_a_path_line_edit.text(), self.merger_ui.pdf_file_b_path_line_edit.text()])

        pdf_merge_manager.write_into_new_pdf_file(self.merger_ui.result_pdf_file_path_line_edit.text())

    # birleştirilen pdf dosyalarının bulunduğu klasörü açan fonksiyon. 
    def set_pdf_result_path_clicked(self): self.merger_ui.result_pdf_file_path_line_edit.setText(MainModel.start_folder_browser(self.merger_ui, "SELECT SECOND FILE") + "/merged_pdf_result.pdf") 
