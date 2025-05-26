from PIL import Image

class PDFConverter: 
    def __init__(self):
        self.selected_file_path = None  # Seçilen dosya yolu
        
        self.result_file_path = None # Sonuç dosyası yolu

     # Bu kısımda makinede yüklü uygulamalar kontrol edilecek ve ilgili fonksiyon çalıştırılacak.

    # Eğer makinede PowerPoint yüklü ise .pptx dosyasını .pdf dosyasına çevirir.
    def convert_pptx_to_pdf_with_powerpoint(self): print(".pptx to .pdf[PowerPoint]")

    # Eğer makinede LibreOffice yüklü ise .pptx dosyasını .pdf dosyasına çevirir. 
    def convert_pptx_to_pdf_with_libreoffice(self): print(".pptx to .pdf[libreoffice]")

    # API kullanarak .pptx dosyasını .pdf dosyasına dönüştürür.
    def conver_to_ppt_to_pdf_with_api(self): print(".pptx to .pdf[API]")

    def convert_image_to_pdf(self):
        try: Image.open(self.selected_file_path).convert("RGB").save(self.result_file_path, "PDF")
        except Exception as ConversionError: return None