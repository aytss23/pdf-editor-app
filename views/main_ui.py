from PyQt5.QtWidgets import QMainWindow, QTableWidget
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.uic import loadUi
from models.main_model import MainModel

class PDFEditorMainUI(QMainWindow): #QMainWindow sınıfından türetilen PDFEditorMainUI sınıfı.

    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.
        
        self.init_ui() # arayüz dosyasını içeri aktarma fonksiyonunu çağır.

        # table view özellikleri.
        self.recent_pdfs_table_view_model = QStandardItemModel() # tablo görünümü için standart öğe modeli oluştur.
        
        self.recent_pdfs_table_view.setModel(self.recent_pdfs_table_view_model) # tablo görünümüne standart öğe modelini ata.
        
        self.recent_pdfs_table_view_model.setHorizontalHeaderLabels(['FILE_PATH', 'LAST_EXEC_TIME']) # tablo görünümündeki başlıkları ayarla.
        
        self.recent_pdfs_table_view.setEditTriggers(QTableWidget.NoEditTriggers) #son açılan pdf'lerin tablosunu düzenlemeye kapat. 
        
        self.recent_pdfs_table_view.setColumnWidth(0, 350) # ikinci sütunun genişliğini ayarla.
        self.recent_pdfs_table_view.setColumnWidth(1, 120) # üçüncü sütunun genişliğini ayarla.
        
        self.update_recent_pdfs_table_view() # tablo görünümünü güncelleme fonksiyonunu çağır.


    # arayüz dosyasını içeri aktar. 
    def init_ui(self): loadUi('views\\resources\\ui\\main_ui.ui', self)

    
    # arayüz bileşenlerini güncelle. 
    def update_recent_pdfs_table_view(self):
        
        self.recent_pdfs_table_view_model.removeRows(0, self.recent_pdfs_table_view_model.rowCount())

        main_model = MainModel()

        #database_manager.log_recent_pdfs([["sample.pdf", "2025-05-10 12:53:56"],["sample2.pdf", "2025-05-10 13:12:32"]])

        recent_pdfs_data = main_model.get_recent_pdfs()

        recent_path_data = []
        displayed_recent_data = []

        for recent_data_index in range(len(recent_pdfs_data)):
            recent_path_data.append(recent_pdfs_data[recent_data_index][0])

        for row_data in recent_pdfs_data:
            if row_data[0] in displayed_recent_data: continue 

            row = [QStandardItem(str(item)) for item in row_data]
        
            self.recent_pdfs_table_view_model.appendRow(row) 
            
            displayed_recent_data.append(row_data[0])

    # uygulamayı kapat.
    def close_app(self): self.close()

