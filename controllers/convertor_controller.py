from models.convertor_model import PDFConverter
from models.main_model import MainModel

from views.convertor_ui import PDFConverterUI

class ConvertorController(): # PDFConvertorUI sınıfından bir ConvertorController sınıfı oluştur.
    def __init__(self): 

        self.converter_ui = PDFConverterUI() # Arayüz sınıfından nesne türet.
        
        self.converter_model = PDFConverter() # Model sınıfından nesne türet.

        self.set_widget_signals() # arayüz bileşenlerinin özelliklerini ayarla.

        self.converter_ui.show() # arayüzü göster. 

    # arayüz bileşenlerinin özelliklerini ayarla. 
    def set_widget_signals(self): 
        
        self.converter_ui.browse_pdf_file_push_button.clicked.connect(self.browse_pdf_file_push_button_clicked) #dosya tarayıcı butonu tıklanınca ilgili fonksiyonu çağır.

        self.converter_ui.convert_to_pdf_push_button.clicked.connect(self.convert_to_pdf_push_button_clicked) #pdf'e dönüştürme butonu tıklandığında ilgili fonksiyonu çağır.

        self.converter_ui.set_result_path_push_button.clicked.connect(self.set_result_path_push_button_clicked) #dosya yolu tarayıcısı butonu tıklanınca ilgili fonksiyonu çağır.

    # Dosya tarayıcı butonu tıklandığında çalışan fonksiyon.
    def browse_pdf_file_push_button_clicked(self): self.converter_ui.selected_file_path_line_edit.setText(MainModel.start_file_browser(self.converter_ui, "SELECT A FILE", "PNG Files (*.png), JPG Files (*.jpg)")[0]) 

    # PDF'e dönüştür butonu tıklandığında çalışan fonksiyon.
    def convert_to_pdf_push_button_clicked(self): 
        self.converter_model.selected_file_path = self.converter_ui.selected_file_path_line_edit.text()
        self.converter_model.result_file_path = self.converter_ui.result_pdf_file_path_line_edit.text()
        
        self.converter_model.convert_image_to_pdf()
    
    # Sonuç dosyası yolu seçme butonu tıklanınca çalışan fonksiyon.
    def set_result_path_push_button_clicked(self): self.converter_ui.result_pdf_file_path_line_edit.setText(MainModel.start_folder_browser(self.converter_ui, "SELEC A RESULT FOLDER"))
