import random
import sys
import io
from PyQt6 import uic
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QMainWindow
from random import randint


class YellowCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.resize(800, 600)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)


    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw(self, qp):


        qp.setBrush(QColor(255, 0, 0))
        size = random.randint(1, 300)
        qp.drawEllipse(100, 100, size, size)


app = QApplication(sys.argv)
win = YellowCircle()
win.show()
sys.exit(app.exec())
