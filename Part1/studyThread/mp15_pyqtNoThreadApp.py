import sys
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * # QIcon
from PyQt5.QtCore import *

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./studyThread/ThreadApp.ui', self)
        self.setWindowIcon(QIcon('./studyThread/arrows.png'))
        self.setWindowTitle('노스레드 앱 v0.3')
        self.pgbTask.setValue(0)

        self.btnStart.clicked.connect(self.btnStartClicked)

    def btnStartClicked(self):
        self.pgbTask.setRange(0, 999999)
        for i in range(0, 100000):
            print(f'노스레드 출력 -> {i}')
            self.pgbTask.setValue(i)
            self.txblog.append(f'노스레드 출력 -> {i}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())