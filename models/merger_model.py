from PyPDF2 import PdfMerger
class PDFMerger:
    def __init__(self): 
        self.pdf_merge_manager = PdfMerger() # PdfMerger sınıfndan nesne türet.

    # İki PDF dosyasını art arda ekleyen fonksiyon.
    def merger_two_pdfs(self, file_paths):
        for pdf_file_path in file_paths: self.pdf_merge_manager.append(pdf_file_path)

    # PDF dosyalarını tek bir dosyaya yazan fonksiyon.
    def write_into_new_pdf_file(self, new_file_path='pdf_editor_merge_result.pdf'):
        try: self.pdf_merge_manager.write(new_file_path)
        
        except Exception: return False 
        
        return True
    
    # Kullanılan dosyaları kapatan ve belleği temizleyen fonksiyon.
    def close_merge_manager(self): self.pdf_merge_manager.close()
    