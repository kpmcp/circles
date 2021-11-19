import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('git_and_circles.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        self.initUI()
        self.do_paint = False

    def initUI(self):
        self.draw_circle_btn.clicked.connect(self.paint)
        print(self.size())

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        x, y = randint(1, 800), randint(1, 400)
        w = randint(1, 200)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, w, w)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
