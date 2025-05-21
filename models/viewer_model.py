import fitz as PDFLoader
from PyQt5.QtGui import QImage, QPixmap
class PDFViewer:
    def __init__(self, pdf_file_path): 
        
        self.selected_file = PDFLoader.open(pdf_file_path) # yolu verilen PDF dosyasını içeri aktar.

    # PDF dosyasının verilen sayfasını görüntüye çevir.
    def get_page_pixmap(self, page_num): 
        
        selected_page = self.selected_file.load_page(page_num)

        page_pixmap = selected_page.get_pixmap()

        return QPixmap.fromImage(QImage(page_pixmap.samples, page_pixmap.width, page_pixmap.height, page_pixmap.stride, QImage.Format_RGBA8888 if page_pixmap.alpha else QImage.Format_RGB888))

    # PDF dosyasının sayfa sayısını döndürür.
    def get_max_page_data(self): return int(self.selected_file.page_count)