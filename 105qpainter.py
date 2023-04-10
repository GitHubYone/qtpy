import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader

class CustomWidget(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing) # アンチエイリアスを有効化する
        pen = QPen(QColor(255, 0, 0))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawEllipse(50, 50, 100, 100) # 中心座標(75, 75)、直径50の円を描画する

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Qt Designerで作成した.uiファイルをロードする
        loader = QUiLoader()
        ui_file = QFile("mainwindow.ui")
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file)
        ui_file.close()

        # カスタムウィジェットを作成して、ウィンドウに追加する
        custom_widget = CustomWidget(self.window)
        custom_widget.setGeometry(50, 50, 300, 300)
        self.window.layout().addWidget(custom_widget)

        self.setCentralWidget(self.window)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
