import sqlite3 
import datetime

DATABASE_PATH = '..\\recent\\recent_pdfs.db' # Veritabanı dosya yolu
TABLE_NAME = 'recent_pdfs' # Veritabanı tablosu adı

class RecentPDFDatabaseManager: # veritabanı yöneticisi sınıfı.

    def __init__(self): self.connect_database() # veritabanı bağlantısını başlat.

    # son kullanılan PDF dosyalarının tutulduğu veritabanına bağlan.
    def connect_database(self): 

        # Veritabanında tablo yoksa oluştur
        def create_table_if_not_exists():
            self.database_cursor.execute(f''' CREATE TABLE IF NOT EXISTS {TABLE_NAME} 
                                         (LOG_ID INTEGER PRIMARY KEY AUTOINCREMENT, FILE_PATH TEXT NOT NULL, LAST_EXEC_TIME TIMESTAMP DEFAULT CURRENT_TIMESTAMP) ''')
            self.database_connection.commit()

        self.database_connection = sqlite3.connect(DATABASE_PATH) # SQLite veritabanı bağlantısını oluştur.

        self.database_cursor = self.database_connection.cursor() # Veritabanı imleci oluştur.
            
        create_table_if_not_exists()

    # veritabanı bağlantısını kapat.
    def close_database(self): 
        del self.database_cursor
        self.database_connection.close()

    # son kullanılan PDF dosyalarını veritabanından temizle. 
    def clear_recent_logs(self): 
        self.database_cursor.execute(f""" DELETE FROM {TABLE_NAME}""") # veritabanı tablosundaki herşeyi sil.
        
        self.database_connection.commit() # veritabanındaki değişiklikleri kaydet. 

    # son kullanılan PDF dosyalarını veritabanına ekle.
    def log_recent_pdfs(self, recent_pdf_data):  
        self.database_cursor.execute(f'INSERT INTO {TABLE_NAME} (FILE_PATH, LAST_EXEC_TIME) VALUES (?, ?)', (recent_pdf_data, str(datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")))) # vertabanında ekleme sorgusunu çalıştır.
        
        self.database_connection.commit() # Veritabanı değişikliklerini kaydet.

    # son kullanılan PDF dosyalarını veritabanından oku.
    def get_recent_pdfs(self): 
        self.database_connection.commit()
        
        return self.database_cursor.execute(f'SELECT FILE_PATH, LAST_EXEC_TIME FROM {TABLE_NAME} ORDER BY LAST_EXEC_TIME DESC').fetchall() #vertabanında okuma sorgusunu çalıştır ve sonuçlarını döndür.
        

#test kodu
#database_manager = RecentPDFDatabaseManager() # veritabanı yöneticisi nesnesi oluştur.

#database_manager.log_recent_pdfs([{'FILE_PATH': 'C:/Users/username/Documents/sample4.pdf', 'LAST_EXEC_TIME': '2023-10-03 12:00:00'},{'FILE_PATH': 'C:/Users/username/Documents/sample3.pdf', 'LAST_EXEC_TIME': '2023-10-04 12:00:00'}]) # son kullanılan PDF dosyalarını veritabanına ekle.

#print(database_manager.get_recent_pdfs()) # son kullanılan PDF dosyalarını veritabanından oku.

#database_manager.close_database() # veritabanı bağlantısını kapat.