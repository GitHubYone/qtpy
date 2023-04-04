# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication,QWidget,QPushButton

class Madoka(QWidget):
    def __init__(self):
        super().__init__()
        css = '''
        background-color: #e7869f;
        color: #635d81;
        font-family: Kaiti SC;
        font-weight: bold;
        font-size: 36px;
        font-style: italic;
        text-decoration: underline;
        '''
        self.setStyleSheet(css)
        botan = QPushButton('第二ボタン',self)
        css = '''
        background-color: #fae4cb;
        border: 3px solid red;
        text-align: right;
        padding: 15px;
        '''
        botan.setStyleSheet(css)
        botan.setGeometry(20,20,250,110)

qAp = QApplication(sys.argv)
mado = Madoka()
mado.show()
qAp.exec()