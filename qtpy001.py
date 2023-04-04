# -*- coding: utf-8 -*-
import sys
import os
import csv
import cv2
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from ui_qtpy001 import Ui_Dialog

class Test(QDialog):
    def __init__(self,parent=None):
        super(Test, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # ウィンドウの位置とサイズを指定（px単位）
        xPos = 50  # x座標
        yPos = 150  # y座標
        windowWidth = 700   # ウィンドウの横幅
        windowHeight = 700  # ウィンドウの高さ
        # ウィンドウの位置とサイズの変更
        self.setGeometry(xPos, yPos, windowWidth, windowHeight)
        self.setWindowFlags(Qt.FramelessWindowHint)

        with open('./moji.csv') as f:
            reader = csv.reader(f)
            for self.row in reader:
                print(self.row)

        self.pb1 = self.ui.pushButton_1.clicked.connect(self.button1)
        self.pb2 = self.ui.pushButton_2.clicked.connect(self.button2)
        self.pb3 = self.ui.pushButton_3.clicked.connect(self.button3)
        self.pb4 = self.ui.pushButton_4.clicked.connect(self.button4)
        self.pb5 = self.ui.pushButton_5.clicked.connect(self.button5)
        self.pb6 = self.ui.pushButton_6.clicked.connect(self.button6)

        global ImageFile
        ImageFile = []
        ImageFile.append(r'./moji01.png')
        ImageFile.append(r'./moji02.png')


    def button1(self):
        labelStyle = """QLabel {
            color:            #FF00AA;  /* 文字色 */
            font-size:        36px;     /* 文字サイズ */
            background-color: #FFAA00;  /* 背景色 */
        }"""
        # 見た目の設定をラベルに反映させる
        self.ui.label.setStyleSheet(labelStyle)
        #self.ui.label.setFont(QFont(""))
        self.ui.label.setText(self.row[0])
        self.ui.label_2.setStyleSheet("background-color:blue;")
        image = QPixmap(ImageFile[0])
        self.ui.label_2.setPixmap(image)


    def button2(self):
        labelStyle = """QLabel {
            color:              black;    /* 文字色 */
            font-size:          24px;     /* 文字サイズ */
            background-color:   yellow;   /* 背景色 */
        }"""
        # 見た目の設定をラベルに反映させるS
        self.ui.label.setStyleSheet(labelStyle)
        self.ui.label.setFont(QFont("klee"))
        self.ui.label.setText(self.row[1])
        self.ui.label_2.setStyleSheet("background-color:black;")
        image = QPixmap(r"./moji02.png")
        self.ui.label_2.setPixmap(image)


    def button3(self):
        # 見た目の設定をラベルに反映させるS
        self.ui.label.setStyleSheet("color:white;font-size:24px;background-color:black;")
        self.ui.label.setText(self.row[2])

    def button4(self):
        self.ui.label.setStyleSheet("color:white;font-size:24px;background-color:black;")
        self.ui.label.setFont(QFont("Osaka"))
        self.ui.label.setText(self.row[3])

    def button5(self):
        self.ui.label.setStyleSheet("color:white;font-size:24px;background-color:black;")
        self.ui.label.setText(self.row[4])

    def button6(self):
        self.ui.label.setStyleSheet("color:white;font-size:24px;background-color:black;")
        self.ui.label.setText(self.row[5])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    #sys.exit(app.exec_())
    try:
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        print("Window closed by keyboard input.")
        sys.exit(app.exec_())
