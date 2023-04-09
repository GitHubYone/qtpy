# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qtpy001.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGraphicsView, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.NonModal)
        Dialog.resize(700, 700)
        Dialog.setMinimumSize(QSize(320, 240))
        Dialog.setMaximumSize(QSize(800, 800))
        palette = QPalette()
        brush = QBrush(QColor(70, 75, 74, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        Dialog.setPalette(palette)
        font = QFont()
        font.setPointSize(6)
        Dialog.setFont(font)
        Dialog.setMouseTracking(False)
        Dialog.setStyleSheet(u"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 20, 71, 31))
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.pushButton_end = QPushButton(Dialog)
        self.pushButton_end.setObjectName(u"pushButton_end")
        self.pushButton_end.setGeometry(QRect(10, 10, 75, 61))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(350, 10, 111, 321))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_1 = QPushButton(self.layoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setInputMethodHints(Qt.ImhHiddenText)
        self.pushButton_1.setAutoDefault(True)

        self.verticalLayout.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.graphicsView = QGraphicsView(Dialog)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(20, 230, 301, 231))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 110, 281, 101))
        self.button = QPushButton(Dialog)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(350, 370, 100, 32))

        self.retranslateUi(Dialog)
        self.label.linkHovered.connect(self.label.setText)
        self.pushButton_end.clicked.connect(Dialog.close)

        self.pushButton_1.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"qt training", None))
#if QT_CONFIG(statustip)
        Dialog.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Dialog.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        Dialog.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.pushButton_end.setText(QCoreApplication.translate("Dialog", u"end", None))
#if QT_CONFIG(statustip)
        self.pushButton_1.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.pushButton_1.setAccessibleDescription(QCoreApplication.translate("Dialog", u"test", None))
#endif // QT_CONFIG(accessibility)
        self.pushButton_1.setText(QCoreApplication.translate("Dialog", u"test1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"test2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"test3", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"test4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"test5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"test6", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.button.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
    # retranslateUi

