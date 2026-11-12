import sys, argparse, shlex
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

class Task7(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("form7.ui", self)
        self.btnRun.clicked.connect(self.run)

    def run(self):
        args_str = self.editArgs.text()
        sys.argv = ["prog"] + shlex.split(args_str)
        
        parser = argparse.ArgumentParser()
        parser.add_argument('params', nargs='*')
        args = parser.parse_args()

        if not args.params:
            self.textOutput.setPlainText("no args")
        else:
            self.textOutput.setPlainText("\n".join(args.params))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task7(); w.show(); sys.exit(app.exec_())