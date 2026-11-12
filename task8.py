import sys, argparse, shlex
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

class Task8(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("form8.ui", self)
        self.btnCalc.clicked.connect(self.calc)

    def calc(self):
        args_str = self.editNums.text()
        sys.argv = ["prog"] + shlex.split(args_str)
        
        parser = argparse.ArgumentParser()
        parser.add_argument('numbers', nargs='*', type=int)
        
        try:
            args = parser.parse_args()
            nums = args.numbers
            if len(nums) == 0: self.textOutput.setPlainText("NO PARAMS")
            elif len(nums) == 1: self.textOutput.setPlainText("TOO FEW PARAMS")
            elif len(nums) > 2: self.textOutput.setPlainText("TOO MANY PARAMS")
            else: self.textOutput.setPlainText(str(nums[0] + nums[1]))
        except SystemExit:
            self.textOutput.setPlainText("ValueError")
        except Exception as e:
            self.textOutput.setPlainText(type(e).__name__)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task8(); w.show(); sys.exit(app.exec_())