# -*- coding: utf-8 -*-

import os
import sys

from PySide6.QtCore import (
                            QCoreApplication,#
                            QDate,
                            QDateTime,
                            QLocale,
                            QMetaObject,
                            QObject,
                            QPoint,
                            QRect,
                            QSize,
                            QTime,
                            QUrl,
                            Qt)
from PySide6.QtGui import (
                            QBrush,
                            QColor,
                            QConicalGradient,
                            QCursor,
                            QFont,
                            QFontDatabase,
                            QGradient,
                            QIcon,
                            QImage,
                            QKeySequence,
                            QLinearGradient,
                            QPainter,
                            QPalette,
                            QPixmap,
                            QRadialGradient,
                            QTransform)
from PySide6.QtWidgets import (
                                QAbstractButton,
                                QApplication,
                                QDialog,
                                QDialogButtonBox,
                                QMainWindow,
                                QPushButton,
                                QFrame,
                                QLabel,
                                QSizePolicy,
                                QWidget)

# Subclass QMainWindow to customize your application's main window
# PySide6のアプリ本体（ユーザがコーディングしていく部分）
class MainWindow(QWidget):              # ウインドウ系クラスを継承すること
    def __init__(self, parent=None):    # parentは他にウインドウを表示させる場合
        #親クラスの初期化
        super().__init__(parent)        # 継承元クラス（ここではQWidget）を初期化

        self.setWindowTitle("PySide6 Training")   #ウインドウタイトル
        # ウィンドウの位置とサイズを指定（px単位）
        xPos = 100  # x座標
        yPos = 300  # y座標
        windowWidth = 600   # ウィンドウの横幅
        windowHeight = 200  # ウィンドウの高さ
        # ウィンドウの位置とサイズの変更
        self.setGeometry(xPos, yPos, windowWidth, windowHeight)
        # ウィンドウサイズの固定
        #self.setFixedSize(windowWidth, windowHeight)

        # ボタンを表示するメソッド
        self.SetButton()

    # ボタンは別のメソッドに分けました
    def SetButton(self):
        # ボタンを使うことを宣言
        button = QPushButton(self)

        # ボタンに表示する文字
        button.setText("押してみよう！！")

        # ボタンを押したら実行させる処理
        # connectメソッド: 処理させるメソッド
        button.pressed.connect(self.CallbackButtonPressed)

        # ボタンを離したら実行させる処理（引数を指定する場合）
        # connectメソッド: 処理させるメソッド
        button.released.connect(lambda: self.CallbackButtonReleased(90))

    # ボタンが押されたら実行させるメソッド
    # connectメソッドから呼び出される
    def CallbackButtonPressed(self):
        print("やりますねぇ")

    # ボタンが離されたら実行させるメソッド（引数あり）
    # connectメソッドから呼び出される
    def CallbackButtonReleased(self, radian):
        print("横向くんだよ" + str(radian) + "度！")


if __name__ == "__main__":

    # 環境変数にPySide6を登録
    # dirname = os.path.dirname(PySide6.__file__)
    # plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    # os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

    app = QApplication(sys.argv)    # PySide6の実行
    window = MainWindow()           # ユーザがコーディングしたクラス
    window.show()                   # PySide6のウィンドウを表示
    sys.exit(app.exec())            # PySide6の終了
    #app.exec_()
