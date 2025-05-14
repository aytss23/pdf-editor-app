from PyQt5.QtWidgets import QMainWindow, QTableWidget, QFileDialog
from PyQt5 import uic 
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from recent import RecentPDFDatabaseManager
from merge import PDFMerger
from split import PDFSplitter   
from reader import PDFReader
from editor import PDFEditor
from convert import PDFConverter

import sys

class PDFConverterUI(QMainWindow): #QMainWindow sınıfından türetilen PDFConverterUI sınıfı
    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.


class PDFEditorUI(QMainWindow): #QMainWindow sınıfından türetilen PDFEditorUI sınıfı
    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.

        self.init_ui() # arayüzü içeri aktarma fonksiyonun çağır.

        self.set_widget_properties() # arayüz bileşenlerinin özelliklerini ayarlama fonksiyonlarını çağır. 

        self.set_edit_properties() # PDF Düzenleme özelliklerini ayarlama fonksiyonunu çağır.


    # arayüzü içeri aktarma fonksiyonu.
    def init_ui(self): uic.loadUi("..\\ui\\editor_ui.ui", self)

    # arayüz bileşenlerinin özelliklerini ayarla.
    def set_widget_properties(self):

        self.file_browser_push_button.clicked.connect(self.file_browser_push_button_clicked) # dosya tarayıcı butonu tıklandığında ilgili fonksiyonu çağır.

        self.set_edit_push_button.clicked.connect(self.set_edit_push_button_clicked) # düzenleme açık/kapalı butonu tıklandığında ilgili fonksiyonu çağır.

        self.set_pen_color_push_button.clicked.connect(self.set_pen_color_push_button_clicked) # kalem rengi seçme butonu tıklandığında ilgili fonksiyonu çağır.

        self.set_pen_size_push_button.clicked.connect(self.set_pen_size_push_button_clicked) # kalem boyutu seçme butonu tıklandığında ilgili fonksiyonu çağır.

    # PDF Düzenleme özelliklerini ayarla.
    def set_edit_properties(self): 
        
        self.set_edit = None # PDF düzenleme özelliğini aç/kapa değişkeni.

        if self.set_edit_push_button.text() == 'EDIT - ON': self.set_edit = True

        else: self.set_edit = False

        self.pen_colors = ['COLOR - BLACK','COLOR - RED','COLOR - BLUE','COLOR - GREEN','COLOR - WHITE'] # kalem renkleri listesi. 
        
        self.pen_sizes = ['SIZE - LIGHT', 'SIZE - NORMAL', 'SIZE - BOLD'] # kalem boyutunun listesi. 

    # dosya tarayıcı butonuna tıklandığında çağrılan fonksiyon.
    def file_browser_push_button_clicked(self): return None

    # dosya düzenleme açık/kapalı butonuna tıklandığında çağrılan fonksiyon.
    def set_edit_push_button_clicked(self): 
        if self.set_edit_push_button.text() == 'EDIT - ON': self.set_edit_push_button.setText('EDIT - OFF')
        
        else: self.set_edit_push_button.setText('EDIT - ON')
        
        print(self.set_edit_push_button.text())

        self.set_edit_properties()

    # kalem rengi seçme butonuna tıklandığında çağrılan fonksiyon.
    def set_pen_color_push_button_clicked(self):
        
        current_pen_color = self.set_pen_color_push_button.text()
        
        print(self.set_pen_color_push_button.text())
        
        for color_index in range(len(self.pen_colors)): 
            if self.pen_colors[color_index] == current_pen_color:
                if color_index == 4: self.set_pen_color_push_button.setText(self.pen_colors[0]) 
                else: self.set_pen_color_push_button.setText(self.pen_colors[color_index + 1])

        self.set_edit_properties()

    # kalem boyutu seçme butonuna tıklandığına çağrılan fonksiyon.
    def set_pen_size_push_button_clicked(self): 

        current_pen_size = self.set_pen_size_push_button.text()

        print(self.set_pen_size_push_button.text())

        for size_index in range(len(self.pen_sizes)):
            if self.pen_sizes[size_index] == current_pen_size:
                if size_index == 2: self.set_pen_size_push_button.setText(self.pen_sizes[0]) 
                else: self.set_pen_size_push_button.setText(self.pen_sizes[size_index + 1])

        self.set_edit_properties()

class PDFMergerUI(QMainWindow): #QMainWindow sınıfından türetilen PDFMergerUI sınıfı
    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.

        self.init_ui() # arayüzü içeri aktarma fonksiyonun çağır.

        self.set_widget_properties() # arayüz bileşenlerinin özelliklerini ayarlama fonksiyonlarını çağır.

    # arayüzü içeri aktarma fonksiyonu
    def init_ui(self): uic.loadUi('..\\ui\\merge_ui.ui', self)

    # arayüz bileşenlerinin özelliklerini ayarla.
    def set_widget_properties(self):

        self.browse_pdf_file_a_push_button.clicked.connect(self.browse_pdf_file_a_push_button_clicked) # PDF dosyası A butonuna tıklandığında browse_pdf_file_a_push_button_clicked fonksiyonunu çağır.

        self.browse_pdf_file_b_push_button.clicked.connect(self.browse_pdf_file_b_push_button_clicked) # PDF dosyası B butonuna tıklandığında browse_pdf_file_b_push_button_clicked fonksiyonunu çağır.

        self.merge_pdfs_push_button.clicked.connect(self.merge_pdfs_push_button_clicked) # PDF dosyalarını birleştir butonuna tıklandığında merge_pdf_push_button_clicked fonksiyonunu çağır.

        self.set_pdf_result_path_push_button.clicked.connect(self.set_pdf_result_path_clicked)
    
    # dosya tarayıcı A butonuna tıklandığında çağrılan fonksiyon.
    def browse_pdf_file_a_push_button_clicked(self): self.pdf_file_a_path_line_edit.setText(str(QFileDialog.getOpenFileName(self, "SELECT FIRST FILE", "","PDF Files (*.pdf)")[0])) 

    # dosya tarayıcı B butonuna tıklandığında çağrılan fonksiyon.
    def browse_pdf_file_b_push_button_clicked(self): self.pdf_file_b_path_line_edit.setText(str(QFileDialog.getOpenFileName(self, "SELECT SECOND FILE", "","PDF Files (*.pdf)")[0]))

    # pdf birleştirme butonuna tıklandığında çağrılan fonksiyon.
    def merge_pdfs_push_button_clicked(self): 
        pdf_merge_manager = PDFMerger()

        pdf_merge_manager.merger_two_pdfs([self.pdf_file_a_path_line_edit.text(), self.pdf_file_b_path_line_edit.text()])

        pdf_merge_manager.write_into_new_pdf_file(self.result_pdf_file_path_line_edit.text())

    # birleştirilen pdf dosyalarının bulunduğu klasörü açan fonksiyon. 
    def set_pdf_result_path_clicked(self): self.result_pdf_file_path_line_edit.setText(f"{QFileDialog.getExistingDirectory(self, 'SET RESULT FOLDER')}/merged_pdfs_result.pdf") 

class PDFSplitterUI(QMainWindow): #QMainWindow sınıfından türetilen PDFParserUI sınıfı
    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.

        self.init_ui() # arayüzü içeri aktarma fonksiyonunu çağır.

        self.set_widget_properties() # arayüz bileşenlerinin özelliklerini ayarlama fonksiyonunu çağır.

    def init_ui(self): uic.loadUi("..\\ui\\split_ui.ui", self) #arayüzü içeri aktar.

    # arayüz bileşenlerinin özelliklerini ayarla.
    def set_widget_properties(self): 

        self.browse_pdf_file_push_button.clicked.connect(self.browse_pdf_file_push_button_clicked) # dosya tarayıcı butonuna tıklandığında ilgili fonksiyonu çağır.

        self.split_pdf_file_push_button.clicked.connect(self.split_pdf_file_push_button_clicked) # dosya parçalama butonu tıklanınca ilgili fonksiyonu çağır.

        self.set_pdf_file_result_path_push_button.clicked.connect(self.set_pdf_file_result_path_push_button_clicked) # dosya tarayıcı butonu tıklandığında ilgili fonksiyonu çağır.

    # dosya tarayıcı butonuna tıklanınca çağrılan fonksiyon.
    def browse_pdf_file_push_button_clicked(self): self.pdf_file_path_line_edit.setText(QFileDialog.getOpenFileName(self, "SELECT '.pdf' FILE", "", "PDF Files (*.pdf)")[0])

    # sonuç dosyası yolu tarayıcı butonu tıklanınca çağrılan fonksiyon.
    def set_pdf_file_result_path_push_button_clicked(self): self.result_pdf_file_path_line_edit.setText(QFileDialog.getExistingDirectory(self, "SELECT RESULT FOLDER") + "/split_pdf_file_result.pdf") 

    # dosya parçalama butonu tıklanınca çağrılan fonksiyon.
    def split_pdf_file_push_button_clicked(self): 
        pdf_splitter = PDFSplitter() # PDFSplitter sınıfından nesne oluştur.

        # Yolu verilen PDF dosyasından belirli sayfaları ayır ve yolu verilen farklı bir dosyaya yaz.
        pdf_splitter.extract_selected_pages_range(self.pdf_file_path_line_edit.text(), int(self.start_page_line_edit.text()), int(self.end_page_line_edit.text()), self.result_pdf_file_path_line_edit.text()) 

        self.log_recent_pdf_file(self.result_pdf_file_path_line_edit.text()) # son kullanulan PDF dosyasını veritabanına kaydet. 

    # son kullanılan PDF Dosyasını veritabanına kaydet.
    def log_recent_pdf_file(self, recent_pdf_file_path): 
        database_manager = RecentPDFDatabaseManager()

        database_manager.log_recent_pdfs(recent_pdf_file_path)

        database_manager.close_database()

class PDFReaderUI(QMainWindow): #QMainWindow sınıfından türetilen PDFReaderUI sınıfı
    def __init__(self, parent = None): 
        super().__init__(parent) # QMainWindow sınıfını başlat.

        self.init_ui() # arayüz dosyasını içeri aktarma fonksiyonunu çağır.
        self.set_widget_properties() # arayüz bileşenlerinin özelliklerini ayarlama fonksiyonunu çağır.

    # arayüz dosyasını içeri aktar.
    def init_ui(self): uic.loadUi('..\\ui\\reader_ui.ui', self)

    # arayüz bileşenlerinin özelliklerini ayarla.
    def set_widget_properties(self): 

        self.browse_file_push_button.clicked.connect(self.browse_file_push_button_clicked) # dosya tarayıcı butonuna tıklandığında browse_file_push_button_clicked fonksiyonunu çağır.
    
        self.next_page_push_button.clicked.connect(self.next_page_push_button_clicked) # sonraki sayfa butonuna tıklandığında next_page_push_button_clicked fonksiyonunu çağır.
    
        self.previous_page_push_button.clicked.connect(self.previous_page_push_button_clicked) # önceki sayfa butonuna tıklandığında previous_page_push_button_clicked fonksiyonunu çağır.

        self.zoom_in_push_button.clicked.connect(self.zoom_in_push_button_clicked) # yakınlaştırma butonuna tıklandığında zoom_in_push_button_clicked fonksiyonunu çağır.

        self.zoom_out_push_button.clicked.connect(self.zoom_out_push_button_clicked) # uzaklaştırma butonuna tıklandığında zoom_out_push_button_clicked fonksiyonunu çağır.

        self.go_to_page_push_button.clicked.connect(self.go_to_page_push_button_clicked) # sayfaya git butonuna tıklandığında go_to_page_push_button_clicked fonksiyonunu çağır.
    
    # son kullanılan PDF Dosyasını veritabanına kaydet.
    def log_recent_pdf_file(self, recent_pdf_file_path): 
        database_manager = RecentPDFDatabaseManager()

        database_manager.log_recent_pdfs(recent_pdf_file_path)

        database_manager.close_database()

    # dosya tarayıcı butonuna tıklandığında çağrılan fonksiyon.
    def browse_file_push_button_clicked(self):
        selected_file_path, _ = QFileDialog.getOpenFileName(self, "SELECT '.pdf' FILE", "", "PDF Files (*.pdf)")  

        self.log_recent_pdf_file(str(selected_file_path))


    # sonraki sayfa butonuna tıklandığında çağrılan fonksiyon.
    def next_page_push_button_clicked(self): pass 

    # önceki sayfa butonuna tıklandığında çağrılan fonksiyon.
    def previous_page_push_button_clicked(self): pass

    # yakınlaştırma butonuna tıklandığında çağrılan fonksiyon.
    def zoom_in_push_button_clicked(self): pass

    # uzaklaştırma butonuna tıklandığında çağrılan fonksiyon.
    def zoom_out_push_button_clicked(self): pass

    # sayfaya git butonuna tıklandığında çağrılan fonksiyon.
    def go_to_page_push_button_clicked(self): pass 


class PDFEditorMainUI(QMainWindow): #QMainWindow sınıfından türetilen PDFEditorMainUI sınıfı.

    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.
        
        self.init_ui() # arayüz dosyasını içeri aktarma fonksiyonunu çağır.

        self.set_widget_properties() # arayüz bileşenlerinin özelliklerini ayarlama fonksiyonunu çağır.

        self.update_recent_pdfs_table_view() # tablo görünümünü güncelleme fonksiyonunu çağır.

    # arayüz dosyasını içeri aktar. 
    def init_ui(self): uic.loadUi('..\\ui\\main_ui.ui', self)

    # arayüz bileşenlerinin özelliklerini tanımla.
    def set_widget_properties(self): 
        # table view özellikleri.
        self.recent_pdfs_table_view_model = QStandardItemModel() # tablo görünümü için standart öğe modeli oluştur.
        
        self.recent_pdfs_table_view.setModel(self.recent_pdfs_table_view_model) # tablo görünümüne standart öğe modelini ata.
        
        self.recent_pdfs_table_view_model.setHorizontalHeaderLabels(['FILE_PATH', 'LAST_EXEC_TIME']) # tablo görünümündeki başlıkları ayarla.
        
        self.recent_pdfs_table_view.setEditTriggers(QTableWidget.NoEditTriggers) #son açılan pdf'lerin tablosunu düzenlemeye kapat. 
        
        self.recent_pdfs_table_view.setColumnWidth(0, 350) # ikinci sütunun genişliğini ayarla.
        self.recent_pdfs_table_view.setColumnWidth(1, 120) # üçüncü sütunun genişliğini ayarla.

        # buton fonksiyonları. 
        self.reader_push_button.clicked.connect(self.reader_push_button_clicked) # PDF okuyucu butonuna tıklandığında reader_push_button_clicked fonksiyonunu çağır.

        self.editor_push_button.clicked.connect(self.editor_push_button_clicked) # PDF düzenleyici butonuna tıklandığında editor_push_button_clicked fonksiyonunu çağır.

        self.merger_push_button.clicked.connect(self.merger_push_button_clicked) # PDF birleştirici butonuna tıklandığında merger_push_button_clicked fonksiyonunu çağır.

        self.parser_push_button.clicked.connect(self.parser_push_button_clicked) # PDF ayrıştırıcı butonuna tıklandığında parser_push_button_clicked fonksiyonunu çağır.

        self.converter_push_button.clicked.connect(self.converter_push_button_clicked) # PDF dönüştürücü butonuna tıklandığında converter_push_button_clicked fonksiyonunu çağır.

        self.exit_push_button.clicked.connect(self.exit_push_button_clicked) # Çıkış butonuna tıklandığında exit_push_button_clicked fonksiyonunu çağır.

        self.clear_recent_pdf_files_push_button.clicked.connect(self.clear_recent_pdf_files_push_button_clicked)


    # arayüz bileşenlerine olay işleyicileri ekle.
    def clear_recent_pdf_files_push_button_clicked(self): 
        database_manager = RecentPDFDatabaseManager() #vertabanına erişmek için nesne oluştur.

        database_manager.clear_recent_logs() # veritabanı tablosundaki tüm verileri silme fonksiyonunu çalıştır.

        database_manager.close_database() # veritabanı bağlantısını kapat.
    
        self.update_recent_pdfs_table_view() # veritabanını tablosunu temizledikten sonra son kullanılan dosyaların tablosunu yenile.

    def reader_push_button_clicked(self): 
        pdf_reader_main = PDFReader()

        self.pdf_reader_win = PDFReaderUI() # PDF okuyucu arayüzü için yeni bir QMainWindow nesnesi oluştur.
        
        self.pdf_reader_win.show() 

    def editor_push_button_clicked(self): 
        pdf_editor_main = PDFEditor()

        self.pdf_editor_win = PDFEditorUI() # PDF Düzenleyici arayüzü için yeni bir QMainWindow nesnesi oluştur.

        self.pdf_editor_win.show()

    def merger_push_button_clicked(self): 
        self.merge_pdfs_win = PDFMergerUI() # PDF birleştirici arayüzü için yeni bir QMainWindow nesnesi oluştur.
        
        self.merge_pdfs_win.show()

    def parser_push_button_clicked(self): 
        self.pdf_splitter = PDFSplitterUI()

        self.pdf_splitter.show()

    def converter_push_button_clicked(self): pdf_converter_main = PDFConverter()

    def exit_push_button_clicked(self): self.close() # uygulamayı kapat.


    # arayüz bileşenlerini güncelle. 
    def update_recent_pdfs_table_view(self):
        
        database_manager = RecentPDFDatabaseManager()
        
        #database_manager.log_recent_pdfs([["sample.pdf", "2025-05-10 12:53:56"],["sample2.pdf", "2025-05-10 13:12:32"]])

        recent_pdfs_data = database_manager.get_recent_pdfs()
        
        recent_path_data = []
        displayed_recent_data = []

        for recent_data_index in range(len(recent_pdfs_data)):
            recent_path_data.append(recent_pdfs_data[recent_data_index][0])

        print(recent_path_data)

        for row_data in recent_pdfs_data:
            if row_data[0] in displayed_recent_data: continue 

            row = [QStandardItem(str(item)) for item in row_data]
        
            self.recent_pdfs_table_view_model.appendRow(row) 
            
            displayed_recent_data.append(row_data[0])

        database_manager.close_database()


