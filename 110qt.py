# -*- coding: utf-8 -*-

import os
import sys
import cv2
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class VideoPlayer(QWidget):
#class VideoPlayer(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus) # キーボードフォーカスを設定

        # ビデオキャプチャーオブジェクトの作成
        self.cap = cv2.VideoCapture()

        # UI要素の作成
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(5,5,1280,720)
        self.filename_label1 = QtWidgets.QLabel(self)
        self.filename_label1.move(5, 900)
        self.filename_label2 = QtWidgets.QLabel(self)
        self.filename_label2.move(10, 1000)

        # ウィンドウの設定
        xPos = 0  # x座標
        yPos = 0  # y座標
        windowWidth = 1920   # ウィンドウの横幅
        windowHeight = 1080  # ウィンドウの高さ
        self.setGeometry(xPos, yPos, windowWidth, windowHeight)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: yellow;")

        # タイマーの作成
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.play)


    def load_video(self, filename):
        # ビデオをロードして再生する準備をする
        filename = ("./dualHA_BSH2.mp4")
        self.cap.open(filename)
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.current_frame = 0
        self.filename_label1.setText(filename)
        self.filename_label2.setText(filename)

        # タイマーを開始
        self.timer.start(1000/self.fps)

    def play(self):
        # ビデオフレームを読み取り、表示する
        ret, frame = self.cap.read()
        if ret:
            self.current_frame += 1
            if self.current_frame >= self.total_frames:
                self.current_frame = 0
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(image)
            self.label.setPixmap(pixmap)
        else:
            # ビデオ再生が終了したらタイマーを停止する
            self.timer.stop()
            self.cap.release()

    def contextMenuEvent(self, event):
        # 右クリックされた場所の座標を取得
        pos = event.pos()

        # QMenuを作成
        menu = QMenu(self)

        # QMenuにQActionを追加
        newAction = QAction('New', self)
        menu.addAction(newAction)

        openAction = QAction('Open', self)
        menu.addAction(openAction)

        quitAction = QAction('Quit', self)
        menu.addAction(quitAction)

        # 右クリックされた場所にQMenuを表示
        menu.move(self.mapToGlobal(pos))
        menu.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape: # Escapeキーが押された場合
            self.close() # アプリケーションを終了
        if event.key() == Qt.Key_Q: # Qキーが押された場合
            self.close() # アプリケーションを終了


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    player = VideoPlayer()
    player.load_video('')
    player.show()
    sys.exit(app.exec_())

