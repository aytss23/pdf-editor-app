from pypdf import PdfReader, PdfWriter # PyPDF2 modülünden PdfReader ve PdfWriter sınıflarını koda dahil et.

class PDFSplitter: # PDF dosyalarını parçalayan veya bir kısmını ayrıştıran sınıf.
    def __init__(self): pass 

    
    # parçalamak için sayfa aralıklarını al.
    def extract_selected_pages_range(self,target_file_path, start_page, end_page, output_file_path="pdf_editor_splitted_result.pdf"):
        pdf_reader = PdfReader(target_file_path) # PdfReader sınıfından nesne türet.
        pdf_writer = PdfWriter() # PdfWriter sınıfından nesne türet.

        page_count = len(pdf_reader.pages)

        if start_page >= 1 and start_page < end_page and end_page <= page_count:

            for extraceted_page_index in range(start_page - 1, end_page):
                pdf_writer.add_page(pdf_reader.pages[extraceted_page_index])

            with open(output_file_path, "wb") as output_file: 
                pdf_writer.write(output_file)

                self.set_output_file_properties(output_file_path)


    # çıktı dosyasının özelliklerini ayarla.
    def set_output_file_properties(self, file_name): return file_name 