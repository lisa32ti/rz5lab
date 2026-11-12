import sys, os, shutil
from datetime import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox

class Task4(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("form4.ui", self)
        self.src, self.dest = "", ""
        self.btnSrc.clicked.connect(lambda: self.set_path('src'))
        self.btnDest.clicked.connect(lambda: self.set_path('dest'))
        self.btnGo.clicked.connect(self.archive)

    def set_path(self, t):
        p = QFileDialog.getExistingDirectory(self, "Выбрать папку")
        if p:
            if t == 'src': self.src = p
            else: self.dest = p
            self.labelInfo.setText(f"Src: {self.src}\nDest: {self.dest}")

    def archive(self):
        if not self.src or not self.dest: return
        t = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        base = os.path.join(self.dest, f"backup_{t}")
        try:
            res = shutil.make_archive(base, 'zip', self.src)
            QMessageBox.information(self, "Успех", f"Создано:\n{res}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task4(); w.show(); sys.exit(app.exec_())