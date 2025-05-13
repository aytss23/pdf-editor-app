import sys
import fitz  # PyMuPDF
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QPushButton, QSpinBox,
    QHBoxLayout, QVBoxLayout, QWidget, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
)
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPixmap, QImage, QPainter


class PDFGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setRenderHint(QPainter.Antialiasing)
        self.zoom = 1.0
        self.zoom_step = 0.1
        self.zoom_max = 5
        self.zoom_min = 0.2

    
    def wheelEvent(self, event):
        # Fare pozisyonuna göre odak noktası ayarla
        old_pos = self.mapToScene(event.pos())

        if event.angleDelta().y() > 0 and self.zoom < self.zoom_max:
            self.zoom += self.zoom_step
        elif event.angleDelta().y() < 0 and self.zoom > self.zoom_min:
            self.zoom -= self.zoom_step
        else:
            return  # zoom sınırı aşıldıysa hiçbir şey yapma

        # Transform'u sıfırla ve yeni zoom'u uygula
        self.resetTransform()
        self.scale(self.zoom, self.zoom)

        # Zoom sonrası fare odak noktasını koru
        new_pos = self.mapToScene(event.pos())
        delta = new_pos - old_pos
        self.translate(delta.x(), delta.y())

class PDFViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fare Destekli PDF Görüntüleyici")
        self.setGeometry(100, 100, 900, 700)

        self.doc = None
        self.current_page = 0
        self.zoom = 1.0

        self.view = PDFGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        # Kontroller
        self.open_btn = QPushButton("PDF Aç")
        self.prev_btn = QPushButton("Önceki")
        self.next_btn = QPushButton("Sonraki")
        self.goto_btn = QPushButton("Git")
        self.page_input = QSpinBox()
        self.page_input.setMinimum(1)
        self.page_input.setMaximum(1)

        self.open_btn.clicked.connect(self.open_pdf)
        self.prev_btn.clicked.connect(self.show_prev_page)
        self.next_btn.clicked.connect(self.show_next_page)
        self.goto_btn.clicked.connect(self.goto_page)

        controls = QHBoxLayout()
        controls.addWidget(self.open_btn)
        controls.addWidget(self.prev_btn)
        controls.addWidget(self.next_btn)
        controls.addWidget(self.page_input)
        controls.addWidget(self.goto_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.view)
        layout.addLayout(controls)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_pdf(self):
        path, _ = QFileDialog.getOpenFileName(self, "PDF Seç", "", "PDF Files (*.pdf)")
        if path:
            self.doc = fitz.open(path)
            self.current_page = 0
            self.page_input.setMaximum(len(self.doc))
            self.page_input.setValue(1)
            self.show_page(self.current_page)

    def show_page(self, page_number):
        if not self.doc or page_number < 0 or page_number >= len(self.doc):
            return

        page = self.doc.load_page(page_number)
        mat = fitz.Matrix(2, 2)  # başlangıç çözünürlüğü
        pix = page.get_pixmap(matrix=mat)

        image = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)

        self.scene.clear()
        self.scene.addItem(QGraphicsPixmapItem(pixmap))
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
        self.zoom = 1.0
        self.view.setTransform(self.view.transform().fromScale(self.zoom, self.zoom))

    def show_next_page(self):
        if self.doc and self.current_page < len(self.doc) - 1:
            self.current_page += 1
            self.page_input.setValue(self.current_page + 1)
            self.show_page(self.current_page)

    def show_prev_page(self):
        if self.doc and self.current_page > 0:
            self.current_page -= 1
            self.page_input.setValue(self.current_page + 1)
            self.show_page(self.current_page)

    def goto_page(self):
        page_number = self.page_input.value() - 1
        if self.doc and 0 <= page_number < len(self.doc):
            self.current_page = page_number
            self.show_page(self.current_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = PDFViewer()
    viewer.show()
    sys.exit(app.exec_())
