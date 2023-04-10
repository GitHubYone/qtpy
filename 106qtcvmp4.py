# -*- coding: utf-8 -*-

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import cv2

class VideoPlayer(QWidget):
    def __init__(self, filename):
        super().__init__()

        # ウィンドウの設定
        self.setWindowTitle('Video Player')
        self.setGeometry(100, 100, 1380, 820)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # ビデオキャプチャの設定
        #self.capture = cv2.VideoCapture("C:\ywork\qtpy\dualHA_BSH2.mp4")
        self.capture = cv2.VideoCapture("./dualHA_BSH2.mp4")
        self.fps = self.capture.get(cv2.CAP_PROP_FPS)

        # ラベルの設定
        self.label1 = QLabel(self)
        self.label1.setGeometry(30, 30, 1280, 720)

        # タイマーの設定
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000/self.fps)

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.label1.setPixmap(QPixmap.fromImage(img))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer('sample.mp4')
    player.show()
    sys.exit(app.exec_())
