from views.merge_ui import PDFMergerUI
from models.main_model import MainModel
from models.merger_model import PDFMerger

class MergerController(PDFMergerUI):
    def __init__(self):
        super().__init__()

        self.show() # arayüzü göster.

        self.set_widget_properties() # arayüz bileşenlerinin özelliklerini ayarlama fonksiyonunu çağır.

        # arayüz bileşenlerinin özelliklerini ayarla.
    def set_widget_properties(self):

        self.browse_pdf_file_a_push_button.clicked.connect(self.browse_pdf_file_a_push_button_clicked) # PDF dosyası A butonuna tıklandığında browse_pdf_file_a_push_button_clicked fonksiyonunu çağır.

        self.browse_pdf_file_b_push_button.clicked.connect(self.browse_pdf_file_b_push_button_clicked) # PDF dosyası B butonuna tıklandığında browse_pdf_file_b_push_button_clicked fonksiyonunu çağır.

        self.merge_pdfs_push_button.clicked.connect(self.merge_pdfs_push_button_clicked) # PDF dosyalarını birleştir butonuna tıklandığında merge_pdf_push_button_clicked fonksiyonunu çağır.

        self.set_pdf_result_path_push_button.clicked.connect(self.set_pdf_result_path_clicked)
    
    # dosya tarayıcı A butonuna tıklandığında çağrılan fonksiyon.
    def browse_pdf_file_a_push_button_clicked(self): self.pdf_file_a_path_line_edit.setText(MainModel.start_file_browser(self, "SELECT FIRST FILE","PDF Files (*.pdf)")[0]) 

    # dosya tarayıcı B butonuna tıklandığında çağrılan fonksiyon.
    def browse_pdf_file_b_push_button_clicked(self): self.pdf_file_b_path_line_edit.setText(MainModel.start_file_browser(self, "SELECT SECOND FILE", "PDF Files (*.pdf)")[0])

    # pdf birleştirme butonuna tıklandığında çağrılan fonksiyon.
    def merge_pdfs_push_button_clicked(self): 
        pdf_merge_manager = PDFMerger()

        pdf_merge_manager.merger_two_pdfs([self.pdf_file_a_path_line_edit.text(), self.pdf_file_b_path_line_edit.text()])

        pdf_merge_manager.write_into_new_pdf_file(self.result_pdf_file_path_line_edit.text())

    # birleştirilen pdf dosyalarının bulunduğu klasörü açan fonksiyon. 
    def set_pdf_result_path_clicked(self): self.result_pdf_file_path_line_edit.setText(MainModel.start_folder_browser(self, "SELECT SECOND FILE") + "/merged_pdf_result.pdf") 
