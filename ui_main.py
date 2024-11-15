# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
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
    Qt,
)
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
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 480)
        MainWindow.setMinimumSize(QSize(320, 480))
        MainWindow.setMaximumSize(QSize(320, 480))
        MainWindow.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnResult = QPushButton(self.centralwidget)
        self.btnResult.setObjectName("btnResult")
        self.btnResult.setGeometry(QRect(10, 70, 140, 30))
        self.btnResult.setMinimumSize(QSize(140, 30))
        self.btnResult.setMaximumSize(QSize(140, 30))
        self.btnResult.setStyleSheet("font-size: 16px;")
        self.btnClear = QPushButton(self.centralwidget)
        self.btnClear.setObjectName("btnClear")
        self.btnClear.setGeometry(QRect(170, 70, 140, 30))
        self.btnClear.setMinimumSize(QSize(140, 30))
        self.btnClear.setMaximumSize(QSize(140, 30))
        self.btnClear.setStyleSheet("font-size: 16px;\n" "")
        self.txtResult = QLabel(self.centralwidget)
        self.txtResult.setObjectName("txtResult")
        self.txtResult.setGeometry(QRect(10, 120, 300, 30))
        self.txtResult.setMinimumSize(QSize(300, 30))
        self.txtResult.setMaximumSize(QSize(300, 30))
        self.txtResult.setStyleSheet(
            'font: 14pt "Segoe UI";\n'
            "background-color: rgb(255, 255, 255);\n"
            "padding-left: 5px;"
        )
        self.txt_lineEdit = QLineEdit(self.centralwidget)
        self.txt_lineEdit.setObjectName("txt_lineEdit")
        self.txt_lineEdit.setGeometry(QRect(10, 21, 300, 30))
        self.txt_lineEdit.setMinimumSize(QSize(300, 30))
        self.txt_lineEdit.setMaximumSize(QSize(300, 30))
        self.txt_lineEdit.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "font-size: 16px;"
        )
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "test_project", None)
        )
        self.btnResult.setText(QCoreApplication.translate("MainWindow", "Result", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", "Clear", None))
        self.txtResult.setText("")

    # retranslateUi
