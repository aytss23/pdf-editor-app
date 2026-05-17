import os
import threading
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QGridLayout, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QFileDialog, QPushButton, QSizePolicy
from PyQt5.QtGui import QBrush, QPixmap
from core.eng import RenderEngine

class DocDisplay(QWidget):
    """Her sekme için bağımsız View ve Engine taşıyan yapı."""
    render_done = pyqtSignal(object)

    def __init__(self, path, controller):
        super().__init__()
        self.controller = controller
        self.engine = RenderEngine()
        self.engine.target_path = path
        self.is_rendering = False
        
        # Arayüz Bileşenleri
        self.layout = QGridLayout(self)
        self.view = QGraphicsView()
        self.view.setDragMode(QGraphicsView.ScrollHandDrag)
        self.view.wheelEvent = lambda e: self.controller.handle_wheel(e)
        
        try: self.view.setBackgroundBrush(QBrush(QPixmap(os.path.join("assets", "icons", "background-grid.png"))))
        except Exception as fexc: pass 
        
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        self.pixmap_item = QGraphicsPixmapItem()
        self.pixmap_item.setTransformationMode(Qt.SmoothTransformation)
        self.scene.addItem(self.pixmap_item)
        self.layout.addWidget(self.view)

        self.render_done.connect(self._update_screen)
        if self.engine.load_doc(): self.refresh()

    def refresh(self):
        """Arka planda render tetikler."""
        if self.is_rendering: return
        self.is_rendering = True
        threading.Thread(target=self._run_render, daemon=True).start()

    def _run_render(self):
        pix = self.engine.render_page()
        self.render_done.emit(pix)

    def _update_screen(self, pixmap):
        if pixmap:
            self.pixmap_item.setPixmap(pixmap)
            self.scene.setSceneRect(0, 0, pixmap.width(), pixmap.height())
        self.is_rendering = False

class AppController:
    """Sinyalleri yakalayan ve motoru tetikleyen ana kontrolcü."""
    def __init__(self, main_ui, _):
        self.ui = main_ui
        self._init_ui()
        self._bind_all_signals()

    def _init_ui(self):
        self.ui.tabWidget.clear()
        self.ui.tabWidget.setTabsClosable(True)
        self.ui.tabWidget.tabCloseRequested.connect(self._on_tab_close)
        
        # 1. Başlıktaki sarı arkaplanı temizle (Temanın rengi gelsin)
        self.ui.main_title_label.setStyleSheet("")

        # 2. Üst menünün (frame) 500 piksellik sıkışma sınırını kaldır
        self.ui.frame.setMaximumWidth(16777215)
        
        # 3. Tüm butonlardaki 40 piksellik kilitleri kır ve metne göre esnemesini sağla
        for button in self.ui.frame.findChildren(QPushButton):
            button.setMaximumWidth(16777215)
            button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        # Homepage'i aç ve kapatma butonunu gizle
        self.create_tab("assets\\layouts\\PDF_EDITOR_README.pdf")
        self.ui.tabWidget.tabBar().setTabButton(0, self.ui.tabWidget.tabBar().RightSide, None)

    def _bind_all_signals(self):
        """UI sinyallerini yakalayıcı (handler) fonksiyonlara bağlar."""
        self.ui.file_browser_push_button.clicked.connect(self.handle_file_open)
        self.ui.next_page_push_button.clicked.connect(self.handle_next)
        self.ui.prev_page_push_button.clicked.connect(self.handle_prev)
        self.ui.zoom_in_push_button.clicked.connect(self.handle_zoom_in)
        self.ui.zoom_out_push_button.clicked.connect(self.handle_zoom_out)
        self.ui.page_rleft_push_button.clicked.connect(self.handle_rotate_left)
        self.ui.page_rright_push_button.clicked.connect(self.handle_rotate_right)
        self.ui.current_page_line_edit.returnPressed.connect(self.handle_jump_page)
        self.ui.tabWidget.currentChanged.connect(self.sync_ui_state)

    # --- YAKALAYICI (HANDLER) FONKSİYONLAR ---

    def handle_next(self):
        disp = self.ui.tabWidget.currentWidget()
        if disp:
            disp.engine.step_page(True) # Trigger engine
            disp.refresh()
            self.sync_ui_state()

    def handle_prev(self):
        disp = self.ui.tabWidget.currentWidget()
        if disp:
            disp.engine.step_page(False) # Trigger engine
            disp.refresh()
            self.sync_ui_state()

    def handle_zoom_in(self):
        disp = self.ui.tabWidget.currentWidget()
        if disp:
            disp.engine.step_zoom(True)
            disp.refresh()

    def handle_zoom_out(self):
        disp = self.ui.tabWidget.currentWidget()
        if disp:
            disp.engine.step_zoom(False)
            disp.refresh()

    def handle_rotate_left(self):
        disp = self.ui.tabWidget.currentWidget()
        if disp:
            disp.engine.step_rotation(False)
            disp.refresh()

    def handle_rotate_right(self):
        disp = self.ui.tabWidget.currentWidget()
        if disp:
            disp.engine.step_rotation(True)
            disp.refresh()

    def handle_wheel(self, event):
        """Mouse tekerleği olayını yakalar."""
        if event.angleDelta().y() > 0: self.handle_zoom_in()
        else: self.handle_zoom_out()

    def handle_jump_page(self):
        disp = self.ui.tabWidget.currentWidget()
        if not disp: return
        try:
            p = int(self.ui.current_page_line_edit.text()) - 1
            if 0 <= p < disp.engine.total_page_num:
                disp.engine.curr_page_num = p
                disp.refresh()
        except: pass
        self.sync_ui_state()

    def handle_file_open(self):
        path, _ = QFileDialog.getOpenFileName(None, "PDF Seç", "", "PDF (*.pdf)")
        if path: self.create_tab(path)

    def create_tab(self, path):
        if os.path.exists(path):
            new_disp = DocDisplay(path, self)
            idx = self.ui.tabWidget.addTab(new_disp, os.path.basename(path))
            self.ui.tabWidget.setCurrentIndex(idx)
            self.sync_ui_state()

    def sync_ui_state(self):
        """Üst paneldeki sayfa numaralarını aktif sekmeye göre günceller."""
        disp = self.ui.tabWidget.currentWidget()
        if disp:
            self.ui.current_page_line_edit.setText(str(disp.engine.curr_page_num + 1))
            self.ui.page_count_line_edit.setText(str(disp.engine.total_page_num))

    def _on_tab_close(self, index):
        if index != 0:
            # Önce widget'ı hafızadan temizle
            widget = self.ui.tabWidget.widget(index)
            if widget:
                widget.engine.close_doc() # PDF'i RAM'den at
                widget.deleteLater()      # Qt nesnesini sil
            
            # Sonra arayüzden kaldır
            self.ui.tabWidget.removeTab(index)