from PyQt5.QtWidgets import QMainWindow, QTableWidget
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.uic import loadUi
from models.main_model import MainModel

class PDFEditorMainUI(QMainWindow): #QMainWindow sınıfından türetilen PDFEditorMainUI sınıfı.

    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.
        
        self.init_ui() # arayüz dosyasını içeri aktarma fonksiyonunu çağır.

        # table view model özellikleri. 
        self.recent_pdfs_table_view_model = QStandardItemModel() # tablo görünümü için standart öğe modeli oluştur.
        self.recent_pdfs_table_view.setModel(self.recent_pdfs_table_view_model) # tablo görünümüne standart öğe modelini ata.
        
    # arayüz dosyasını içeri aktar. 
    def init_ui(self): loadUi('views\\resources\\ui\\main_ui.ui', self)

    # Arayüzdeki tablonun özelliklerini ayarla.
    def set_table_view_properties(self):
        self.recent_pdfs_table_view_model.setHorizontalHeaderLabels(['FILE_PATH', 'LAST_EXEC_TIME']) # tablo görünümündeki başlıkları ayarla.        
        
        self.recent_pdfs_table_view.setColumnWidth(0, 350) # ikinci sütunun genişliğini ayarla.
        self.recent_pdfs_table_view.setColumnWidth(1, 120) # üçüncü sütunun genişliğini ayarla.

        self.recent_pdfs_table_view.setEditTriggers(QTableWidget.NoEditTriggers) #son açılan pdf'lerin tablosunu düzenlemeye kapat. 
        
    # arayüz bileşenlerini güncelle. 
    def update_recent_pdfs_table_view(self, recent_pdfs): 
        self.recent_pdfs_table_view_model.clear() # tablodaki veriyi ve özelliklerini sil.
        self.set_table_view_properties() # tablonun özelliklerini ayarla.

        if recent_pdfs == None: return None #Eğer boş veri gelirse güncelleme yapma.  

        # tabloya verileri ekle.
        for row_data in recent_pdfs:
            table_item = [QStandardItem(str(column_data)) for column_data in row_data] # veritabanından alınan satır verilerini QStandartItem verisi listesine dönüştür.
            self.recent_pdfs_table_view_model.appendRow(table_item) # QStandartItem satır verisi listesini tablodaki ilgili satırdaki kolonlara doldur. 

        return True
    
    # uygulamayı kapat.
    def close_app(self): self.close()

