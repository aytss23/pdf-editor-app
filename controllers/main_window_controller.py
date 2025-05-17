import models.merger_model
import models.viewer_model
from views.main_ui import PDFEditorMainUI
from views.convertor_ui import PDFConverterUI
from views.editor_ui import PDFEditorUI
from views.merge_ui import PDFMergerUI
from views.splitter_ui import PDFSplitterUI
from views.viewer_ui import PDFViewerUI

from controllers.merger_controller import MergerController
import models 
from models.main_model import MainModel
from utils.logs import RecentFileLogger

class MainWindowController(PDFEditorMainUI):
    def __init__(self):
        super().__init__()

        self.show()

        self.set_widget_properties()

    # arayüz bileşenlerinin özelliklerini tanımla.
    def set_widget_properties(self): 
        
        # buton fonksiyonları. 
        self.viewer_push_button.clicked.connect(self.viewer_push_button_clicked) # PDF okuyucu butonuna tıklandığında reader_push_button_clicked fonksiyonunu çağır.

        self.editor_push_button.clicked.connect(self.editor_push_button_clicked) # PDF düzenleyici butonuna tıklandığında editor_push_button_clicked fonksiyonunu çağır.

        self.merger_push_button.clicked.connect(self.merger_push_button_clicked) # PDF birleştirici butonuna tıklandığında merger_push_button_clicked fonksiyonunu çağır.

        self.parser_push_button.clicked.connect(self.parser_push_button_clicked) # PDF ayrıştırıcı butonuna tıklandığında parser_push_button_clicked fonksiyonunu çağır.

        self.converter_push_button.clicked.connect(self.converter_push_button_clicked) # PDF dönüştürücü butonuna tıklandığında converter_push_button_clicked fonksiyonunu çağır.

        self.exit_push_button.clicked.connect(self.exit_push_button_clicked) # Çıkış butonuna tıklandığında exit_push_button_clicked fonksiyonunu çağır.

        self.clear_recent_pdf_files_push_button.clicked.connect(self.clear_recent_pdf_files_push_button_clicked)

    # arayüz bileşenlerine olay işleyicileri ekle.
    def clear_recent_pdf_files_push_button_clicked(self): 

        # İş mantığı ve arayüz sınıflarından nesneleri türet.    
        main_model = MainModel()
        main_view = PDFEditorMainUI()

        # veriitabanı tablosundan silme işlemi yap ve arayüzdeki tabloyu güncelle. 
        main_model.delete_recent_pdfs()
        main_view.update_recent_pdfs_table_view()


    def viewer_push_button_clicked(self): 
        viewer_model = models.viewer_model.PDFReader()
         
    def editor_push_button_clicked(self): return None

    def merger_push_button_clicked(self): 
        self.merger_controller = MergerController()

    def parser_push_button_clicked(self): return None

    def converter_push_button_clicked(self): return None

    def exit_push_button_clicked(self): self.close_app() # uygulamayı kapat.


