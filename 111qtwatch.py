import sys
import math
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt, QPoint, QRectF

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('Analog Clock')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawClock(qp)
        qp.end()

    def drawClock(self, qp):
        # 円を描画
        qp.setBrush(QColor(255, 255, 255))
        qp.setPen(QPen(QColor(0, 0, 0), 2))
        rect = QRectF(10, 10, 300, 300)
        qp.drawEllipse(rect)

        # 目盛を描画
        pen = QPen(QColor(0, 0, 0), 2)
        qp.setPen(pen)
        center = QPoint(160, 160)
        r = 120
        for i in range(12):
            angle = math.pi / 6 * i
            x1 = center.x() + r * math.sin(angle)
            y1 = center.y() - r * math.cos(angle)
            x2 = center.x() + (r - 10) * math.sin(angle)
            y2 = center.y() - (r - 10) * math.cos(angle)
            qp.drawLine(x1, y1, x2, y2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
