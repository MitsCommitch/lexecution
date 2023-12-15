# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lexecution.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)
from frontend.assets.public import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1068, 717)
        MainWindow.setMaximumSize(QSize(1920, 1080))
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionConfig = QAction(MainWindow)
        self.actionConfig.setObjectName(u"actionConfig")
        self.actionDefaultBG = QAction(MainWindow)
        self.actionDefaultBG.setObjectName(u"actionDefaultBG")
        self.actionBGImage = QAction(MainWindow)
        self.actionBGImage.setObjectName(u"actionBGImage")
        self.actionFont = QAction(MainWindow)
        self.actionFont.setObjectName(u"actionFont")
        self.actionFontColor = QAction(MainWindow)
        self.actionFontColor.setObjectName(u"actionFontColor")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{border-image: url(:/background/castletext.jpg);}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, -1, -1, 20)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")

        self.gridLayout.addWidget(self.widget_3, 1, 0, 1, 2)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")

        self.gridLayout.addWidget(self.widget_4, 2, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout.addWidget(self.widget_2, 6, 0, 1, 1)

        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")

        self.gridLayout.addWidget(self.widget_5, 0, 3, 1, 1)

        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")

        self.gridLayout.addWidget(self.widget_6, 2, 1, 1, 1)

        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")

        self.gridLayout.addWidget(self.widget_7, 2, 2, 1, 1)

        self.rogue = QLabel(self.centralwidget)
        self.rogue.setObjectName(u"rogue")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rogue.sizePolicy().hasHeightForWidth())
        self.rogue.setSizePolicy(sizePolicy)
        self.rogue.setAutoFillBackground(False)
        #self.rogue.setStyleSheet(u"image: url(:/stickman/0.png)")
        self.rogue_recolor()
        self.rogue.setScaledContents(True)
        self.rogue.setFrameShape(QFrame.StyledPanel)
        self.rogue.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.rogue, 2, 3, 5, 1)

        self.definition = QLabel(self.centralwidget)
        self.definition.setObjectName(u"definition")
        self.definition.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        def_font = QFont()
        def_font.setBold(False)
        self.definition.setFont(def_font)
        self.definition.setTextFormat(Qt.RichText)
        self.definition.setScaledContents(False)
        self.definition.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.definition.setWordWrap(True)

        self.gridLayout.addWidget(self.definition, 3, 0, 1, 3)

        self.rubrick = QLabel(self.centralwidget)
        self.rubrick.setObjectName(u"rubrick")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rubrick.sizePolicy().hasHeightForWidth())
        self.rubrick.setSizePolicy(sizePolicy1)
        rubrick_font = QFont()
        rubrick_font.setBold(True)
        self.rubrick.setFont(rubrick_font)
        self.rubrick.setFrameShadow(QFrame.Plain)
        self.rubrick.setScaledContents(False)
        self.rubrick.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.gridLayout.addWidget(self.rubrick, 4, 0, 1, 3)

        self.used_letters = QLabel(self.centralwidget)
        self.used_letters.setObjectName(u"used_letters")
        sizePolicy.setHeightForWidth(self.used_letters.sizePolicy().hasHeightForWidth())
        self.used_letters.setSizePolicy(sizePolicy)

        used_letters_font = QFont()
        used_letters_font.setBold(True)
        self.used_letters.setFont(used_letters_font)
        self.used_letters.setScaledContents(False)
        self.used_letters.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.used_letters.setWordWrap(True)

        family = self.settings.value('font')
        if not family:
            family = u"Gabriola"
        
        font = QFont(family)

        points = int(self.settings.value('font_size'))
        if not points:
            points = 18

        font_color = self.settings.value('font_color')
        if not font_color:
            font_color = "#000000"

        self.update_font(font=font, font_size=points, font_color=font_color)

        self.gridLayout.addWidget(self.used_letters, 5, 0, 1, 3)

        self.widget_8 = QWidget(self.centralwidget)
        self.widget_8.setObjectName(u"widget_8")

        self.gridLayout.addWidget(self.widget_8, 0, 2, 1, 1)

        self.widget_9 = QWidget(self.centralwidget)
        self.widget_9.setObjectName(u"widget_9")

        self.gridLayout.addWidget(self.widget_9, 1, 2, 1, 1)

        self.widget_10 = QWidget(self.centralwidget)
        self.widget_10.setObjectName(u"widget_10")

        self.gridLayout.addWidget(self.widget_10, 1, 3, 1, 1)

        self.widget_11 = QWidget(self.centralwidget)
        self.widget_11.setObjectName(u"widget_11")

        self.gridLayout.addWidget(self.widget_11, 6, 1, 1, 1)

        self.widget_12 = QWidget(self.centralwidget)
        self.widget_12.setObjectName(u"widget_12")

        self.gridLayout.addWidget(self.widget_12, 6, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1068, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionConfig)
        self.menuEdit.addAction(self.actionFont)
        self.menuEdit.addAction(self.actionFontColor)
        self.menuEdit.addAction(self.actionDefaultBG)
        self.menuEdit.addAction(self.actionBGImage)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lexecution", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionConfig.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.actionFont.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.actionFontColor.setText(QCoreApplication.translate("MainWindow", u"Font Color", None))
        self.actionDefaultBG.setText(QCoreApplication.translate("MainWindow", u"Use Default Background Image"))
        self.actionBGImage.setText(QCoreApplication.translate("MainWindow", u"Set Background Image", None))
        self.definition.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Previous Word<br>Definition</p></body></html>", None))
        self.rubrick.setText(QCoreApplication.translate("MainWindow", u"_ _ _ _ _", None))
        self.used_letters.setText(QCoreApplication.translate("MainWindow", u"Used Letters:", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

