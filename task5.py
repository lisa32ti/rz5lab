import sys
import os
import datetime
import schedule
import time
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QThread, pyqtSignal

class SchedThread(QThread):
    log_signal = pyqtSignal(str)
    
    def run(self):
        def job():
            self.log_signal.emit(f"Ку! (Время: {datetime.datetime.now().strftime('%H:%M:%S')})")
        
        now = datetime.datetime.now()
        hours_left = 24 - now.hour
        times_to_run = min(12, hours_left)

        for i in range(times_to_run):
            target_hour = (now.hour + i + 1) % 24
            target_time = f"{target_hour:02d}:00"
            schedule.every().day.at(target_time).do(job)
            self.log_signal.emit(f"Задача запланирована на {target_time}")
        
        self.log_signal.emit("Ожидание времени...")
        
        while True:
            schedule.run_pending()
            time.sleep(1)


class Task5(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "form5.ui"), self)
        
        self.btnStart.clicked.connect(self.start_scheduler)
        self.thread = SchedThread()
        self.thread.log_signal.connect(self.log)

    def log(self, msg):
        self.textLog.appendPlainText(msg)

    def start_scheduler(self):
        self.btnStart.setEnabled(False)
        self.thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Task5()
    w.show()
    sys.exit(app.exec_())