from models.main_model import MainModel
from views.viewer_ui import PDFViewerUI
from models.viewer_model import PDFViewer


class ViewerController: 
    def __init__(self):

        # Arayüz sınıfından nesne oluştur ve arayüzü göster.
        self.viewer_ui = PDFViewerUI()
        self.viewer_ui.show()
        
        self.viewer_model = PDFViewer() # PDFViewer model-iş mantığı sınıfından nesne türet.

        self.set_widget_signals() # arayüz bileşenelrinin özelliklerini ayarlama fonksiyonunu çağır.

      # arayüz bileşenlerinin özelliklerini ayarla.
    def set_widget_signals(self): 

        self.viewer_ui.browse_file_push_button.clicked.connect(self.browse_file_push_button_clicked) # dosya tarayıcı butonuna tıklandığında browse_file_push_button_clicked fonksiyonunu çağır.
    
        self.viewer_ui.next_page_push_button.clicked.connect(self.next_page_push_button_clicked) # sonraki sayfa butonuna tıklandığında next_page_push_button_clicked fonksiyonunu çağır.
    
        self.viewer_ui.previous_page_push_button.clicked.connect(self.previous_page_push_button_clicked) # önceki sayfa butonuna tıklandığında previous_page_push_button_clicked fonksiyonunu çağır.

        self.viewer_ui.zoom_in_push_button.clicked.connect(self.zoom_in_push_button_clicked) # yakınlaştırma butonuna tıklandığında zoom_in_push_button_clicked fonksiyonunu çağır.

        self.viewer_ui.zoom_out_push_button.clicked.connect(self.zoom_out_push_button_clicked) # uzaklaştırma butonuna tıklandığında zoom_out_push_button_clicked fonksiyonunu çağır.

        self.viewer_ui.go_to_page_push_button.clicked.connect(self.go_to_page_push_button_clicked) # sayfaya git butonuna tıklandığında go_to_page_push_button_clicked fonksiyonunu çağır.

        self.viewer_ui.show_full_screen_push_button.clicked.connect(self.show_full_screen_push_button_clicked)

        self.viewer_ui.page_display_layout.addWidget(self.viewer_model)

    def mouse_wheel_scroolled(self, scroll_event): return None

    def show_full_screen_push_button_clicked(self): self.viewer_ui.set_screensize()
    
    # dosya tarayıcı butonuna tıklandığında çağrılan fonksiyon.
    def browse_file_push_button_clicked(self):
        # PDF dosyası seçimi için dosya tarayıcısını başlat.
        selected_file_path = MainModel.start_file_browser(self.viewer_ui, "SELECT A PDF FILE", "PDF Files (*.pdf)")[0]    
        self.viewer_model.open_pdf_file(selected_file_path) 

        #Seçilen PDF dosyasını son kullanılanlar veritabanına ekle. 
        main_model = MainModel()
        main_model.log_recent_pdf(selected_file_path)

        self.viewer_model.render_selected_page()

        self.viewer_ui.update_page_info(self.viewer_model.selected_page, self.viewer_model.max_page)
    
        
    # sonraki sayfa butonuna tıklandığında çağrılan fonksiyon.
    def next_page_push_button_clicked(self):
        self.viewer_model.check_page_num(1)

        self.viewer_model.render_selected_page()
        
        self.viewer_ui.update_page_info(self.viewer_model.selected_page, self.viewer_model.max_page)

    # önceki sayfa butonuna tıklandığında çağrılan fonksiyon.
    def previous_page_push_button_clicked(self): 
        self.viewer_model.check_page_num(-1)

        self.viewer_model.render_selected_page()

        self.viewer_ui.update_page_info(self.viewer_model.selected_page, self.viewer_model.max_page)

    # yakınlaştırma butonuna tıklandığında çağrılan fonksiyon.
    def zoom_in_push_button_clicked(self): self.viewer_model.zoom_in_page()

    # uzaklaştırma butonuna tıklandığında çağrılan fonksiyon.
    def zoom_out_push_button_clicked(self): 
        self.viewer_model.zoom_out_page()
        
    # sayfaya git butonuna tıklandığında çağrılan fonksiyon.
    def go_to_page_push_button_clicked(self): 
        self.viewer_model.selected_page = int(self.viewer_ui.current_page_line_edit.text()) if self.viewer_model.check_page_num(int(self.viewer_ui.current_page_line_edit.text())) else self.viewer_model.selected_page

        self.viewer_model.render_selected_page()