from PyQt5.QtGui import QImage, QPixmap
import fitz

class RenderEngine:
    def __init__(self) -> None:
        self.target_path = ""
        self.curr_page_num = 0
        self.total_page_num = 0
        self.scale_factor = 1.0
        self.rotation_direct = 0 
        self.pdf_doc = None

    def load_doc(self) -> bool:
        try: 
            self.pdf_doc = fitz.open(self.target_path)
            self.total_page_num = len(self.pdf_doc)
            return True
        except: return False
    
    # --- YÖNETİM FONKSİYONLARI (TRIGGER TARGETS) ---
    
    def step_page(self, forward: bool):
        """Sayfayı ileri veya geri taşır."""
        new_val = self.curr_page_num + (1 if forward else -1)
        if 0 <= new_val < self.total_page_num:
            self.curr_page_num = new_val

    def step_zoom(self, zoom_in: bool):
        """Yakınlaşma veya uzaklaşma yapar (Limitli)."""
        delta = 0.2 if zoom_in else -0.2
        new_scale = self.scale_factor + delta
        if 0.4 <= new_scale <= 5.0: # Profesyonel zoom sınırları
            self.scale_factor = new_scale

    def step_rotation(self, clockwise: bool):
        """Yönü 90 derece döndürür."""
        delta = 90 if clockwise else -90
        self.rotation_direct = (self.rotation_direct + delta) % 360

    def render_page(self) -> QPixmap:
        """Mevcut dahili duruma göre render yapar."""
        if not self.pdf_doc: return None
        try:
            page = self.pdf_doc.load_page(self.curr_page_num)
            mat = fitz.Matrix(self.scale_factor, self.scale_factor).prerotate(self.rotation_direct)
            pix = page.get_pixmap(matrix=mat)
            fmt = QImage.Format_RGBA8888 if pix.alpha else QImage.Format_RGB888
            qimg = QImage(pix.samples, pix.width, pix.height, pix.stride, fmt)
            return QPixmap.fromImage(qimg)
        except: return None
        
    def close_doc(self):
        """C++ seviyesindeki RAM sızıntısını önler."""
        if self.pdf_doc:
            self.pdf_doc.close()
            self.pdf_doc = None