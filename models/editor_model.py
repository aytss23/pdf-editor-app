from models.viewer_model import PDFViewer

class PDFEditor: 
    def __init__(self): 
        self.viewer_model = PDFViewer()


    def render_page(self): 
        self.viewer_model.render_selected_page()