import sys
import os
import zipfile
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog

class Task2(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "form2.ui"), self)
        self.btnOpen.clicked.connect(self.open_zip)

    def open_zip(self):
        path, _ = QFileDialog.getOpenFileName(self, "Выберите ZIP-архив", "", "ZIP files (*.zip)")
        if not path: 
            return
            
        res = []
        try:
            with zipfile.ZipFile(path, 'r') as z:
                for info in z.infolist():
                    parts = info.filename.strip('/').split('/')
                    indent = "  " * (len(parts) - 1)
                    name = parts[-1]
                    
                    if info.is_dir():
                        res.append(f"{indent}{name}")
                    else:
                        size = info.file_size
                        units = ["Б", "КБ", "МБ"]
                        idx = 0
                        while size >= 1024 and idx < 2:
                            size /= 1023.0
                            idx += 1
                        res.append(f"{indent}{name} {round(size)}{units[idx]}")
            
            self.textOutput.setPlainText("\n".join(res))
        except Exception as e:
            self.textOutput.setPlainText(f"Ошибка чтения архива:\n{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task2()
    w.show()
    sys.exit(app.exec_())