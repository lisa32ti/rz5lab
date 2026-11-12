import sys
import os
import textwrap
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox

def format_text_block(frame_height, frame_width, file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        return str(e)
    
    lines = []
    for paragraph in text.split('\n'):
        if not paragraph:
            lines.append("")
        else:
            wrapped = textwrap.wrap(paragraph, width=frame_width)
            lines.extend(wrapped)
            
    result_lines = lines[:frame_height]
    return '\n'.join(result_lines)

class Task10(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "form10.ui"), self)
        
        self.current_file = ""
        self.btnLoad.clicked.connect(self.load_file)
        self.btnFormat.clicked.connect(self.show_formatted)

    def load_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Text files (*.txt);;All files (*)")
        if path:
            self.current_file = path
            self.labelFile.setText(f"Файл: {os.path.basename(path)}")

    def show_formatted(self):
        if not self.current_file:
            QMessageBox.warning(self, "Ошибка", "Сначала выберите файл!")
            return
            
        h = self.spinHeight.value()
        w = self.spinWidth.value()
        
        result = format_text_block(h, w, self.current_file)
        
        self.textOutput.setPlainText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task10()
    w.show()
    sys.exit(app.exec_())