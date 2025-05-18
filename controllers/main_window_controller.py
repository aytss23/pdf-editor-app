from views.main_ui import PDFEditorMainUI

from models.main_model import MainModel

from controllers.merger_controller import MergerController
from controllers.convertor_controller import ConvertorController
from controllers.splitter_controller import SplitterController
from controllers.editor_controller import EditorController
from controllers.viewer_controller import ViewerController


class MainWindowController():
    def __init__(self):
        super().__init__()

        self.main_window_ui = PDFEditorMainUI()
        
        self.main_window_ui.show() # UI sınıfından türetilen arayüzü göster.

        self.set_widget_signals() # arayüz bileşenlerinin özelliklerini ayarlama fonksiyonunu çağır.

        main_model = MainModel()

        self.main_window_ui.update_recent_pdfs_table_view(main_model.update_recent_pdfs())
        
    # arayüz bileşenlerinin özelliklerini tanımla.
    def set_widget_signals(self): 
        
        # buton fonksiyonları. 
        self.main_window_ui.viewer_push_button.clicked.connect(self.viewer_push_button_clicked) # PDF okuyucu butonuna tıklandığında reader_push_button_clicked fonksiyonunu çağır.

        self.main_window_ui.editor_push_button.clicked.connect(self.editor_push_button_clicked) # PDF düzenleyici butonuna tıklandığında editor_push_button_clicked fonksiyonunu çağır.

        self.main_window_ui.merger_push_button.clicked.connect(self.merger_push_button_clicked) # PDF birleştirici butonuna tıklandığında merger_push_button_clicked fonksiyonunu çağır.

        self.main_window_ui.parser_push_button.clicked.connect(self.splitter_push_button_clicked) # PDF ayrıştırıcı butonuna tıklandığında parser_push_button_clicked fonksiyonunu çağır.

        self.main_window_ui.converter_push_button.clicked.connect(self.converter_push_button_clicked) # PDF dönüştürücü butonuna tıklandığında converter_push_button_clicked fonksiyonunu çağır.

        self.main_window_ui.exit_push_button.clicked.connect(self.exit_push_button_clicked) # Çıkış butonuna tıklandığında exit_push_button_clicked fonksiyonunu çağır.

        self.main_window_ui.clear_recent_pdf_files_push_button.clicked.connect(self.clear_recent_pdf_files_push_button_clicked)

    # arayüz bileşenlerine olay işleyicileri ekle.
    def clear_recent_pdf_files_push_button_clicked(self): 

        # İş mantığı ve arayüz sınıflarından nesneleri türet.    
        main_model = MainModel()
        # veriitabanı tablosundan silme işlemi yap ve arayüzdeki tabloyu güncelle. 
        main_model.delete_recent_pdfs()

        self.main_window_ui.update_recent_pdfs_table_view(None)

    # PDF okuma Controller sınıfından nesne türet ve arayüzü başlat.
    def viewer_push_button_clicked(self): self.viewer_controller = ViewerController()

    # PDF düzenleme Controller sınıfından nesne türet ve arayüzü başlat.
    def editor_push_button_clicked(self): return None

    # PDF birleştirme Controller sınıfından nesne türet ve arayüzü başlat.
    def merger_push_button_clicked(self): self.merger_controller = MergerController()

    # PDF parçalama Controller sınıfından nesne türet ve arayüzü başlat.
    def splitter_push_button_clicked(self): self.splitter_controller = SplitterController()

    # PDF dönüştürme Controller sınıfından nesne türet ve arayüzü başlat. 
    def converter_push_button_clicked(self): return None

    # UI sınıfına sinyal gönder ve uygulamayı kapat. 
    def exit_push_button_clicked(self): self.main_window_ui.close_app() # uygulamayı kapat.


