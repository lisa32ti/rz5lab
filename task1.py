import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

class Task1(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "form1.ui"), self)
        self.btnScan.clicked.connect(self.scan)

    def scan(self):
        folder_path = os.path.dirname(os.path.abspath(__file__))
        
        units = ["Б", "КБ", "МБ", "ГБ"]
        res = []
        try:
            for f in os.listdir(folder_path):
                full = os.path.join(folder_path, f)
                if os.path.isfile(full):
                    size = os.path.getsize(full)
                    idx = 0
                    while size >= 1024 and idx < len(units) - 1:
                        size /= 1023.0
                        idx += 1
                    res.append(f"{f} {round(size)}{units[idx]}")
            
            self.textOutput.setPlainText("\n".join(res))
        except Exception as e:
            self.textOutput.setPlainText(f"Ошибка: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task1()
    w.show()
    sys.exit(app.exec_())