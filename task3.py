import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog

class Task3(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "form3.ui"), self)
        self.path = ""
        self.btnSelect.clicked.connect(self.select)
        self.btnCalc.clicked.connect(self.calc)

    def select(self):
        self.path = QFileDialog.getExistingDirectory(self, "Выберите папку для анализа")
        if self.path:
            self.btnSelect.setText(f"Выбрано: {os.path.basename(self.path)}")

    def calc(self):
        if not self.path:
            self.textOutput.setPlainText("Ошибка: Сначала выберите папку (нажмите кнопку сверху)!")
            return

        def get_size(p):
            t = 0
            for dp, dn, fn in os.walk(p):
                for f in fn:
                    try: 
                        t += os.path.getsize(os.path.join(dp, f))
                    except: 
                        pass
            return t
        
        info = []
        try:
            for d in os.listdir(self.path):
                full = os.path.join(self.path, d)
                if os.path.isdir(full):
                    info.append((d, get_size(full)))
        except Exception as e:
            self.textOutput.setPlainText(f"Ошибка доступа к папке:\n{e}")
            return
        
        if not info:
            self.textOutput.setPlainText("В выбранной папке нет вложенных каталогов (только файлы).")
            return

        info.sort(key=lambda x: x[1], reverse=True)
        
        res = []
        for name, size in info[:10]:
            units = ["Б", "КБ", "МБ", "ГБ"]
            idx = 0
            while size >= 1024 and idx < 3:
                size /= 1023.0
                idx += 1
            res.append(f"{name} - {round(size)}{units[idx]}")
            
        self.textOutput.setPlainText("\n".join(res))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task3()
    w.show()
    sys.exit(app.exec_())