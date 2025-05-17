from models.convertor_model import PDFConverter
from views.convertor_ui import PDFConverterUI

class ConvertorController(PDFConverterUI): # PDFConvertorUI sınıfından bir ConvertorController sınıfı oluştur.
    def __init__(self): super().__init__() 

    # arayüz bileşenlerinin özelliklerini ayarla. 
    def set_widget_properties(self): 
        
        self.browse_pdf_file_push_button.clicked.connect(self.browse_pdf_file_push_button_clicked) #dosya tarayıcı butonu tıklanınca ilgili fonksiyonu çağır.

        self.convert_to_pdf_push_button.clicked.connect(self.convert_to_pdf_push_button_clicked) #pdf'e dönüştürme butonu tıklandığında ilgili fonksiyonu çağır.

        self.set_result_path_push_button.clicked.connect(self.set_result_path_push_button_clicked) #dosya yolu tarayıcısı butonu tıklanınca ilgili fonksiyonu çağır.

    # Dosya tarayıcı butonu tıklandığında çalışan fonksiyon.
    def browse_pdf_file_push_button_clicked(self): return None 

    # PDF'e dönüştür butonu tıklandığında çalışan fonksiyon.
    def convert_to_pdf_push_button_clicked(self): return None

    # Sonuç dosyası yolu seçme butonu tıklanınca çalışan fonksiyon.
    def set_result_path_push_button_clicked(self): return None
