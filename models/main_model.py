from utils.logs import RecentFileLogger
from PyQt5.QtWidgets import QFileDialog
import os

class MainModel:
    def __init__(self): pass 
    
    # Dosyaları kontrol yoluna ekle. 
    def append_to_path(self): return None

    # Dosyaları doğrula.
    def confirm_files(self): return None

    # Veritabanından son kullanılan PDF dosyalarını çek.
    def get_recent_pdfs(self): 
        logger = RecentFileLogger()

        return logger.get_recent_pdfs()

    # Son kullanılan PDF dosyalarını veritabanı tablosundan sil. 
    def delete_recent_pdfs(self): 
        db_manager = RecentFileLogger() 
        
        db_manager.delete_recent_pdfs()
        
        db_manager.close_database()

        
    # Son kullanılan PDF dosyalarını veritabanına ekle. 
    def log_recent_pdfs(self, recent_pdfs): 
        logger = RecentFileLogger()

        logger.log_recent_pdfs(recent_pdfs)

        logger.close_database()

    # Bir çıktı dosyasını farklı kaydet.
    @staticmethod
    def save_output_file_as(file_path, new_save_path): return None

    # Dosya tarayıcısını başlat.
    @staticmethod
    def start_file_browser(ui_obj, browser_title, file_filter): return QFileDialog.getOpenFileName(ui_obj, browser_title, "", file_filter)

    # Klasör tarayıcısını başlat.
    @staticmethod
    def start_folder_browser( ui_obj, browser_title): return QFileDialog.getExistingDirectory(ui_obj, browser_title)
