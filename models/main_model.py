from utils.logs import RecentFileLogger
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QStandardItem
import os

class MainModel:
    def __init__(self): self.database_manager = RecentFileLogger() 
    
    # Dosyaları kontrol yoluna ekle. 
    def append_to_path(self): return None

    # Dosyaları doğrula.
    def confirm_files(self): return None

    # Veritabanından son kullanılan PDF dosyalarını çek.
    def get_recent_pdfs(self): return self.database_manager.get_recent_pdfs()

    
    def update_recent_pdfs(self): return self.database_manager.get_recent_pdfs()
        
    # Son kullanılan PDF dosyalarını veritabanı tablosundan sil. 
    def delete_recent_pdfs(self): self.database_manager.delete_recent_pdfs()        
        
    # Son kullanılan PDF dosyalarını veritabanına ekle. 
    def log_recent_pdf(self, recent_pdf): 
        is_already_logged = False
        
        recent_pdfs = self.database_manager.get_recent_pdfs()

        for row_data in range(len(recent_pdfs)):
            if recent_pdf == recent_pdfs[row_data][0]: is_already_logged = True
        

        if not is_already_logged: self.database_manager.log_recent_pdf(recent_pdf)

    # Bir çıktı dosyasını farklı kaydet.
    @staticmethod
    def save_output_file_as(file_path, new_save_path): return None

    # Dosya tarayıcısını başlat.
    @staticmethod
    def start_file_browser(ui_obj, browser_title, file_filter): return QFileDialog.getOpenFileName(ui_obj, browser_title, "", file_filter)

    # Klasör tarayıcısını başlat.
    @staticmethod
    def start_folder_browser( ui_obj, browser_title): return QFileDialog.getExistingDirectory(ui_obj, browser_title)
