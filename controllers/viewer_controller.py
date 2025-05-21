from models.main_model import MainModel
from views.viewer_ui import PDFViewerUI
from models.viewer_model import PDFViewer
class ViewerController: 
    def __init__(self):

        # Arayüz sınıfından nesne oluştur ve arayüzü göster.
        self.viewer_ui = PDFViewerUI()
        self.viewer_ui.show()

        self.set_widget_signals() # arayüz bileşenelrinin özelliklerini ayarlama fonksiyonunu çağır.

      # arayüz bileşenlerinin özelliklerini ayarla.
    def set_widget_signals(self): 

        self.viewer_ui.browse_file_push_button.clicked.connect(self.browse_file_push_button_clicked) # dosya tarayıcı butonuna tıklandığında browse_file_push_button_clicked fonksiyonunu çağır.
    
        self.viewer_ui.next_page_push_button.clicked.connect(self.next_page_push_button_clicked) # sonraki sayfa butonuna tıklandığında next_page_push_button_clicked fonksiyonunu çağır.
    
        self.viewer_ui.previous_page_push_button.clicked.connect(self.previous_page_push_button_clicked) # önceki sayfa butonuna tıklandığında previous_page_push_button_clicked fonksiyonunu çağır.

        self.viewer_ui.zoom_in_push_button.clicked.connect(self.zoom_in_push_button_clicked) # yakınlaştırma butonuna tıklandığında zoom_in_push_button_clicked fonksiyonunu çağır.

        self.viewer_ui.zoom_out_push_button.clicked.connect(self.zoom_out_push_button_clicked) # uzaklaştırma butonuna tıklandığında zoom_out_push_button_clicked fonksiyonunu çağır.

        self.viewer_ui.go_to_page_push_button.clicked.connect(self.go_to_page_push_button_clicked) # sayfaya git butonuna tıklandığında go_to_page_push_button_clicked fonksiyonunu çağır.

    # dosya tarayıcı butonuna tıklandığında çağrılan fonksiyon.
    def browse_file_push_button_clicked(self, selected_file_path = None):
        
        if selected_file_path == None: MainModel.start_file_browser(self.viewer_ui, "SELECT A PDF FILE", "PDF Files (*.pdf)")[0] # PDF dosyası seçimi için dosya tarayıcısını başlat.

        # Seçilen PDF dosyasını son kullanılanlar veritabanına ekle. 
        main_model = MainModel()
        main_model.log_recent_pdf(selected_file_path)
        
        self.viewer_model = PDFViewer(selected_file_path) # PDFViewer model-iş mantığı sınıfından nesne türet.
        self.selected_page = 0 # İlk sayfadan görüntülemeye başla.
        
        self.viewer_ui.display_page_image(self.viewer_model.get_page_pixmap(self.selected_page)) # PDF dosyasının ilgili sayfasını arayüzde görüntüle.

        self.max_page = self.viewer_model.get_max_page_data() - 1 # PDF dosyasının sayfa sayısı.

        self.viewer_ui.update_page_info(self.selected_page, self.max_page)

    # sonraki sayfa butonuna tıklandığında çağrılan fonksiyon.
    def next_page_push_button_clicked(self):
        if self.selected_page == self.max_page: return None
        
        self.selected_page += 1
        self.viewer_ui.display_page_image(self.viewer_model.get_page_pixmap(self.selected_page)) # PDF dosyasının ilgili sayfasını arayüzde görüntüle.

        self.viewer_ui.update_page_info(self.selected_page, self.max_page)
        
    # önceki sayfa butonuna tıklandığında çağrılan fonksiyon.
    def previous_page_push_button_clicked(self): 
        if self.selected_page == 0: return None  # görüntülenecek sayfa numarasını bir azalt.
        
        self.selected_page -= 1
        self.viewer_ui.display_page_image(self.viewer_model.get_page_pixmap(self.selected_page)) # PDF dosyasının ilgili sayfasını arayüzde görüntüle.
        
        self.viewer_ui.update_page_info(self.selected_page, self.max_page)

    # yakınlaştırma butonuna tıklandığında çağrılan fonksiyon.
    def zoom_in_push_button_clicked(self): pass

    # uzaklaştırma butonuna tıklandığında çağrılan fonksiyon.
    def zoom_out_push_button_clicked(self): pass

    # sayfaya git butonuna tıklandığında çağrılan fonksiyon.
    def go_to_page_push_button_clicked(self): 
        target_page = int(self.viewer_ui.current_page_line_edit.text())
        if target_page < self.max_page: self.viewer_ui.display_page_image(self.viewer_model.get_page_pixmap(target_page)) 
