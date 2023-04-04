# -*- coding: utf-8 -*-
import PySide6
from PySide6.QtWidgets import (QApplication,
                               QDialog,         # ダイアログを使うのに必要
                               QLabel,          # ラベルを使うのに必要
                               QPushButton,     # ボタンを使うのに必要
                               QWidget)
import os
import sys


# PySide6のアプリ本体（ユーザがコーディングしていく部分）
class MainWindow(QWidget):
    def __init__(self, parent=None):
        # 親クラスの初期化
        super().__init__(parent)
        
        # ウィンドウタイトル
        self.setWindowTitle("PySide6で作ったアプリです。")
        
        # ボタンを表示するメソッド
        self.SetButton()
        
    # ボタンは別のメソッドに分けました
    def SetButton(self):
        button = QPushButton(self)          # ボタンを使うことを宣言
        button.setText("最近だらしねぇな")  # ボタンに表示する文字
        # ボタンがクリックされたら呼び出す処理
        button.clicked.connect(self.CallbackClickedButton)
        
    # ボタンがクリックされたら実行する処理
    def CallbackClickedButton(self):
        dialog = QDialog()                              # ダイアログを使うことを宣言
        dialog.setWindowTitle("救いはないんですか！？") # ダイアログのタイトル
        
        label = QLabel(dialog)                  # 「ダイアログで」ラベルを使うことを宣言
        label.setText("ホイホイチャーハン")     # ラベルに文字を設定
        label.setStyleSheet("font-size: 32px;") # ラベル文字の大きさ
        
        # ダイアログをラベルの大きさに合わせる
        labelWidth = label.sizeHint().width()   # ラベルの横幅
        labelHeight = label.sizeHint().height() # ラベルの高さ
        dialog.resize(labelWidth, labelHeight)  # ダイアログのサイズ変更
        
        # ダイアログを表示
        dialog.exec()


if __name__ == "__main__":
    # 環境変数にPySide6を登録
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    
    app = QApplication(sys.argv)    # PySide6の実行
    window = MainWindow()           # ユーザがコーディングしたクラス
    window.show()                   # PySide6のウィンドウを表示
    sys.exit(app.exec())            # PySide6の終了