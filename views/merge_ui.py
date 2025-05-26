from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.uic import loadUi 

class PDFMergerUI(QMainWindow): #QMainWindow sınıfından türetilen PDFMergerUI sınıfı
    def __init__(self): 
        super().__init__() # QMainWindow sınıfını başlat.

        self.init_ui() # arayüzü içeri aktarma fonksiyonun çağır.

    # arayüzü içeri aktarma fonksiyonu
    def init_ui(self): loadUi('views\\resources\\ui\\merge_ui.ui', self)
    
    def update_progress_status(self, on_progress: bool = False, is_started: bool = False):

        def set_on_progress():
            self.merge_pdfs_push_button.setEnabled(False)
            
            self.merge_pdfs_push_button.setStyleSheet("background-color: rgb(255, 170, 0); color: white;")

            self.merge_pdfs_push_button.setText("IN PROGRESS")

        def set_completed():
            self.merge_pdfs_push_button.setEnabled(True)
            
            self.merge_pdfs_push_button.setStyleSheet("background-color: rgb(0, 170, 0); color: white;")

            self.merge_pdfs_push_button.setText("COMPLETED")


        def set_default():
            self.merge_pdfs_push_button.setEnabled(True)
            
            self.merge_pdfs_push_button.setStyleSheet("")

            self.merge_pdfs_push_button.setText("MERGE PDF'S")

        if is_started and on_progress: set_on_progress()

        elif is_started and not on_progress: set_completed()

        else: set_default()