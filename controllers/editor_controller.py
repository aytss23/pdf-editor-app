from views.editor_ui import PDFEditorUI
from models.editor_model import PDFEditor
from models.main_model import MainModel

class EditorController():
    def __init__(self): 
        super().__init__()

        self.editor_ui = PDFEditorUI()
        self.editor_model = PDFEditor()
    
        self.set_widget_signals()

        self.editor_ui.show()


    # arayüz bileşenlerinin özelliklerini ayarla.
    def set_widget_signals(self):

        self.editor_ui.file_browser_push_button.clicked.connect(self.file_browser_push_button_clicked) # dosya tarayıcı butonu tıklandığında ilgili fonksiyonu çağır.

        self.editor_ui.set_edit_push_button.clicked.connect(self.set_edit_push_button_clicked) # düzenleme açık/kapalı butonu tıklandığında ilgili fonksiyonu çağır.

        self.editor_ui.set_pen_color_push_button.clicked.connect(self.set_pen_color_push_button_clicked) # kalem rengi seçme butonu tıklandığında ilgili fonksiyonu çağır.

        self.editor_ui.set_pen_size_push_button.clicked.connect(self.set_pen_size_push_button_clicked) # kalem boyutu seçme butonu tıklandığında ilgili fonksiyonu çağır.

    # PDF Düzenleme özelliklerini ayarla.
    def set_edit_properties(self): 
        
        self.set_edit = None # PDF düzenleme özelliğini aç/kapa değişkeni.

        if self.editor_ui.set_edit_push_button.text() == 'EDIT - ON': self.set_edit = True

        else: self.set_edit = False

        self.pen_colors = ['COLOR - BLACK','COLOR - RED','COLOR - BLUE','COLOR - GREEN','COLOR - WHITE'] # kalem renkleri listesi. 
        
        self.pen_sizes = ['SIZE - LIGHT', 'SIZE - NORMAL', 'SIZE - BOLD'] # kalem boyutunun listesi. 

    # dosya tarayıcı butonuna tıklandığında çağrılan fonksiyon.
    def file_browser_push_button_clicked(self): 
        self.editor_model.viewer_model.selected_file = MainModel.start_file_browser(self.editor_ui, "SELECT A '.PDF' FILE", "PDF Files (*.pdf)")[0]

        self.editor_model.render_page()

    # dosya düzenleme açık/kapalı butonuna tıklandığında çağrılan fonksiyon.
    def set_edit_push_button_clicked(self): 
        if self.editor_ui.set_edit_push_button.text() == 'EDIT - ON': self.editor_ui.set_edit_push_button.setText('EDIT - OFF')
        
        else: self.editor_ui.set_edit_push_button.setText('EDIT - ON')
        
        self.set_edit_properties()

    # kalem rengi seçme butonuna tıklandığında çağrılan fonksiyon.
    def set_pen_color_push_button_clicked(self):
        
        current_pen_color = self.editor_ui.set_pen_color_push_button.text()
        
        for color_index in range(len(self.pen_colors)): 
            if self.pen_colors[color_index] == current_pen_color:
                if color_index == 4: self.editor_ui.set_pen_color_push_button.setText(self.pen_colors[0]) 
                else: self.editor_ui.set_pen_color_push_button.setText(self.pen_colors[color_index + 1])

        self.set_edit_properties()

    # kalem boyutu seçme butonuna tıklandığına çağrılan fonksiyon.
    def set_pen_size_push_button_clicked(self): 

        current_pen_size = self.editor_ui.set_pen_size_push_button.text()

        for size_index in range(len(self.pen_sizes)):
            if self.pen_sizes[size_index] == current_pen_size:
                if size_index == 2: self.editor_ui.set_pen_size_push_button.setText(self.pen_sizes[0]) 
                else: self.editor_ui.set_pen_size_push_button.setText(self.pen_sizes[size_index + 1])

        self.set_edit_properties()