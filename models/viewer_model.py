import fitz as PDFLoader
from PyQt5.QtGui import QImage, QPixmap, QLinearGradient, QColor, QBrush
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

class PDFViewer(QGraphicsView):
    def __init__(self): 
        super().__init__()
        
        self.set_view_parameters() # Görüntüleme parametrelerini tanımla.
        
        self.render_scene = QGraphicsScene()
        
        '''
        self.background_gradient = QLinearGradient(0, 0, 400, 600) # Arka plan gradyanı tanımla.
        
        self.background_gradient.setColorAt(0, QColor(255, 255, 255)) # Gradyanın başlangıç rengi beyaz.
        self.background_gradient.setColorAt(1, QColor(0, 0, 0)) # Gradyanın bitiş rengi siyah.

        self.render_scene.setBackgroundBrush(QBrush(self.background_gradient)) # Gradyanı arka plana uygula.
        '''
        
        self.setScene(self.render_scene)
        
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def set_view_parameters(self):
        self.scale_index = 1.0 # Görüntüye yakınlaştırma katsayısı.

        self.selected_page = 0 # PDF Dosyasını 0 (1) sayfadan başlat.

        self.max_page = 1 # PDF dosyasının sayfa sayısı.
        
        self.selected_file = None # Dosya değişkeni.
        

    def open_pdf_file(self, file_path): # PDF dosyasını aç.
        
        self.set_view_parameters()

        self.selected_file  = PDFLoader.open(file_path)
        
        self.max_page = self.selected_file.page_count

    def check_page_num(self, type=0):
        if self.selected_page + type >= 0 and self.selected_page + type < self.max_page: 
            self.selected_page += type
            return True
        else: return False

    # PDF dosyasının verilen sayfasının piksel haritasını döndür.
    def get_page_pixmap(self, page_num, render_matrix): 
        selected_page = self.selected_file.load_page(page_num)
        return selected_page.get_pixmap(matrix = render_matrix)

    # Verilen PDF sayfa piksel haritasını görüntü piksel haritasına çevir.
    def get_image_pixmap(self, img_pixmap): return QPixmap.fromImage(QImage(img_pixmap.samples, img_pixmap.width, img_pixmap.height, img_pixmap.stride, QImage.Format_RGBA8888 if img_pixmap.alpha else QImage.Format_RGB888)) 

    def go_to_selected_page(self): self.render_selected_page() # Direkt olarak seçilen sayfayı görüntüle.

    def render_selected_page(self): # Seçili sayfayı işle ve görüntüle.
    
        render_matrix = PDFLoader.Matrix(self.scale_index, self.scale_index)

        self.render_scene.clear() 

        page_img_pixmap = self.get_image_pixmap(self.get_page_pixmap(self.selected_page, render_matrix))
        
        self.render_scene.addPixmap(page_img_pixmap)

    def zoom_in_page(self): # Sayfaya yakınlaştır.
        if self.scale_index < 3.04: self.scale_index *= 1.25
        self.render_selected_page()

    def zoom_out_page(self): # Sayfadan uzaklaştır.
        if self.scale_index > 0.314: self.scale_index *= 0.75
        self.render_selected_page()