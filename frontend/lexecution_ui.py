# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\code\lexecution\frontend\lexecution2.ui'
#
# Created by: PySide6 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1068, 717)
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget\n"
"{\n"
"     border-image: url(:/background/castletext.jpg);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(20, -1, -1, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 2)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout.addWidget(self.widget_3, 1, 0, 1, 2)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_4, 2, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 6, 0, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout.addWidget(self.widget_5, 0, 3, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout.addWidget(self.widget_6, 2, 1, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.centralwidget)
        self.widget_7.setObjectName("widget_7")
        self.gridLayout.addWidget(self.widget_7, 2, 2, 1, 1)
        self.rogue = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rogue.sizePolicy().hasHeightForWidth())
        self.rogue.setSizePolicy(sizePolicy)
        self.rogue.setAutoFillBackground(False)
        self.rogue.setStyleSheet("image: url(:/stickman/1.png)")
        self.rogue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rogue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rogue.setObjectName("rogue")
        self.gridLayout.addWidget(self.rogue, 2, 3, 5, 1)
        self.definition = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(QtGui.QFont.Weight.Normal)
        self.definition.setFont(font)
        self.definition.setTextFormat(QtCore.Qt.RichText)
        self.definition.setScaledContents(False)
        self.definition.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.definition.setWordWrap(True)
        self.definition.setObjectName("definition")
        self.gridLayout.addWidget(self.definition, 3, 0, 1, 3)
        self.rubrick = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rubrick.sizePolicy().hasHeightForWidth())
        self.rubrick.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.rubrick.setFont(font)
        self.rubrick.setFrameShadow(QtWidgets.QFrame.Plain)
        self.rubrick.setScaledContents(False)
        self.rubrick.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.rubrick.setObjectName("rubrick")
        self.gridLayout.addWidget(self.rubrick, 4, 0, 1, 3)
        self.used_letters = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.used_letters.sizePolicy().hasHeightForWidth())
        self.used_letters.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.used_letters.setFont(font)
        self.used_letters.setScaledContents(False)
        self.used_letters.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.used_letters.setWordWrap(True)
        self.used_letters.setObjectName("used_letters")
        self.gridLayout.addWidget(self.used_letters, 5, 0, 1, 3)
        self.widget_8 = QtWidgets.QWidget(self.centralwidget)
        self.widget_8.setObjectName("widget_8")
        self.gridLayout.addWidget(self.widget_8, 0, 2, 1, 1)
        self.widget_9 = QtWidgets.QWidget(self.centralwidget)
        self.widget_9.setObjectName("widget_9")
        self.gridLayout.addWidget(self.widget_9, 1, 2, 1, 1)
        self.widget_10 = QtWidgets.QWidget(self.centralwidget)
        self.widget_10.setObjectName("widget_10")
        self.gridLayout.addWidget(self.widget_10, 1, 3, 1, 1)
        self.widget_11 = QtWidgets.QWidget(self.centralwidget)
        self.widget_11.setObjectName("widget_11")
        self.gridLayout.addWidget(self.widget_11, 6, 1, 1, 1)
        self.widget_12 = QtWidgets.QWidget(self.centralwidget)
        self.widget_12.setObjectName("widget_12")
        self.gridLayout.addWidget(self.widget_12, 6, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QWidgetAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionExit = QtWidgets.QWidgetAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionConfig = QtWidgets.QWidgetAction(MainWindow)
        self.actionConfig.setObjectName("actionConfig")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionConfig)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lexecution"))
        self.definition.setText(_translate("MainWindow", "<html><head/><body><p>TextLabel</p></body></html>"))
        self.rubrick.setText(_translate("MainWindow", "TextLabel"))
        self.used_letters.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionConfig.setText(_translate("MainWindow", "Config"))
import images_rc
