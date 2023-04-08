from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QBrush, QPen, QColor
from PySide6.QtWidgets import QApplication, QWidget

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(300, 300)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        pen = QPen(QColor(0, 0, 255), 2)
        painter.setPen(pen)
        
        brush = QBrush(QColor(255, 0, 0, 127))
        painter.setBrush(brush)
        
        rect = QRect(50, 50, 200, 200)
        painter.drawRect(rect)
        
if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()

