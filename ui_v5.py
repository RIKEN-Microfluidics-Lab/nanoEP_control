# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_v5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 926)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Trigger_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Trigger_Button.setGeometry(QtCore.QRect(670, 850, 111, 31))
        self.Trigger_Button.setObjectName("Trigger_Button")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 390, 751, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 731, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.WG_Vol2_Edit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.WG_Vol2_Edit.setFont(font)
        self.WG_Vol2_Edit.setObjectName("WG_Vol2_Edit")
        self.gridLayout.addWidget(self.WG_Vol2_Edit, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)
        self.WG_t3_Edit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.WG_t3_Edit.setFont(font)
        self.WG_t3_Edit.setObjectName("WG_t3_Edit")
        self.gridLayout.addWidget(self.WG_t3_Edit, 1, 4, 1, 1)
        self.WG_t2_Edit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.WG_t2_Edit.setFont(font)
        self.WG_t2_Edit.setObjectName("WG_t2_Edit")
        self.gridLayout.addWidget(self.WG_t2_Edit, 1, 3, 1, 1)
        self.WG_t1_Edit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.WG_t1_Edit.setFont(font)
        self.WG_t1_Edit.setObjectName("WG_t1_Edit")
        self.gridLayout.addWidget(self.WG_t1_Edit, 1, 1, 1, 1)
        self.SetWGButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SetWGButton.setFont(font)
        self.SetWGButton.setObjectName("SetWGButton")
        self.gridLayout.addWidget(self.SetWGButton, 1, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)
        self.WG_Vol1_Edit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.WG_Vol1_Edit.setFont(font)
        self.WG_Vol1_Edit.setObjectName("WG_Vol1_Edit")
        self.gridLayout.addWidget(self.WG_Vol1_Edit, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 5, 1, 1)
        self.WG_Cyc_Edit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.WG_Cyc_Edit.setFont(font)
        self.WG_Cyc_Edit.setObjectName("WG_Cyc_Edit")
        self.gridLayout.addWidget(self.WG_Cyc_Edit, 1, 5, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 490, 751, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 731, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Monitor_Button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Monitor_Button.setFont(font)
        self.Monitor_Button.setObjectName("Monitor_Button")
        self.gridLayout_2.addWidget(self.Monitor_Button, 1, 4, 1, 1)
        self.Set_DAQ_Button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Set_DAQ_Button.setFont(font)
        self.Set_DAQ_Button.setObjectName("Set_DAQ_Button")
        self.gridLayout_2.addWidget(self.Set_DAQ_Button, 1, 3, 1, 1)
        self.DAQ_NumSmpl_Edit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DAQ_NumSmpl_Edit.setFont(font)
        self.DAQ_NumSmpl_Edit.setObjectName("DAQ_NumSmpl_Edit")
        self.gridLayout_2.addWidget(self.DAQ_NumSmpl_Edit, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)
        self.DAQ_NumCh_Edit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DAQ_NumCh_Edit.setFont(font)
        self.DAQ_NumCh_Edit.setObjectName("DAQ_NumCh_Edit")
        self.gridLayout_2.addWidget(self.DAQ_NumCh_Edit, 1, 0, 1, 1)
        self.DAQ_Rate_Edit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DAQ_Rate_Edit.setFont(font)
        self.DAQ_Rate_Edit.setObjectName("DAQ_Rate_Edit")
        self.gridLayout_2.addWidget(self.DAQ_Rate_Edit, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 4, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 750, 751, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.Rec_Button = QtWidgets.QPushButton(self.groupBox_3)
        self.Rec_Button.setGeometry(QtCore.QRect(620, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Rec_Button.setFont(font)
        self.Rec_Button.setObjectName("Rec_Button")
        self.Filepath_Edit = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.Filepath_Edit.setGeometry(QtCore.QRect(10, 50, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Filepath_Edit.setFont(font)
        self.Filepath_Edit.setObjectName("Filepath_Edit")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 30, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.Filename_Edit = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.Filename_Edit.setGeometry(QtCore.QRect(380, 50, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Filename_Edit.setFont(font)
        self.Filename_Edit.setObjectName("Filename_Edit")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(380, 30, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.toolButton = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton.setGeometry(QtCore.QRect(340, 60, 25, 19))
        self.toolButton.setObjectName("toolButton")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(50, 860, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(100, 860, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel{\n"
"    background-color:white;\n"
"    color: #ff0000;\n"
"}")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(160, 860, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(210, 860, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel{\n"
"    background-color:white;\n"
"    color: blue;\n"
"}")
        self.label_16.setObjectName("label_16")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 600, 751, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.Motor_message = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.Motor_message.setGeometry(QtCore.QRect(520, 30, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Motor_message.setFont(font)
        self.Motor_message.setObjectName("Motor_message")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_4)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 30, 491, 101))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.DH_Button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DH_Button.setFont(font)
        self.DH_Button.setObjectName("DH_Button")
        self.gridLayout_3.addWidget(self.DH_Button, 0, 2, 1, 1)
        self.MR_Button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MR_Button.setFont(font)
        self.MR_Button.setObjectName("MR_Button")
        self.gridLayout_3.addWidget(self.MR_Button, 0, 1, 1, 1)
        self.GH_Button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GH_Button.setFont(font)
        self.GH_Button.setObjectName("GH_Button")
        self.gridLayout_3.addWidget(self.GH_Button, 1, 2, 1, 1)
        self.MA_Edit = QtWidgets.QTextEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MA_Edit.setFont(font)
        self.MA_Edit.setObjectName("MA_Edit")
        self.gridLayout_3.addWidget(self.MA_Edit, 1, 0, 1, 1)
        self.MN_Button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MN_Button.setFont(font)
        self.MN_Button.setObjectName("MN_Button")
        self.gridLayout_3.addWidget(self.MN_Button, 0, 3, 1, 1)
        self.TP_Button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TP_Button.setFont(font)
        self.TP_Button.setObjectName("TP_Button")
        self.gridLayout_3.addWidget(self.TP_Button, 1, 3, 1, 1)
        self.MA_Button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MA_Button.setFont(font)
        self.MA_Button.setObjectName("MA_Button")
        self.gridLayout_3.addWidget(self.MA_Button, 0, 0, 1, 1)
        self.MR_Edit = QtWidgets.QTextEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MR_Edit.setFont(font)
        self.MR_Edit.setObjectName("MR_Edit")
        self.gridLayout_3.addWidget(self.MR_Edit, 1, 1, 1, 1)
        self.SentCommand_Buttun = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SentCommand_Buttun.setFont(font)
        self.SentCommand_Buttun.setObjectName("SentCommand_Buttun")
        self.gridLayout_3.addWidget(self.SentCommand_Buttun, 2, 0, 1, 4)
        self.Bottom_message = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Bottom_message.setGeometry(QtCore.QRect(270, 850, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Bottom_message.setFont(font)
        self.Bottom_message.setObjectName("Bottom_message")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Rec_Button.clicked.connect(MainWindow.slot1)
        self.SetWGButton.clicked.connect(MainWindow.slot4)
        self.Trigger_Button.clicked.connect(MainWindow.slot5)
        self.Set_DAQ_Button.clicked.connect(MainWindow.slot6)
        self.Monitor_Button.clicked.connect(MainWindow.slot7)
        self.toolButton.clicked.connect(MainWindow.slot8)
        self.MA_Button.clicked.connect(MainWindow.slot9)
        self.MR_Button.clicked.connect(MainWindow.slot10)
        self.DH_Button.clicked.connect(MainWindow.slot11)
        self.GH_Button.clicked.connect(MainWindow.slot12)
        self.MN_Button.clicked.connect(MainWindow.slot13)
        self.TP_Button.clicked.connect(MainWindow.slot14)
        self.SentCommand_Buttun.clicked.connect(MainWindow.slot15)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Trigger_Button.setText(_translate("MainWindow", "trigger"))
        self.groupBox.setTitle(_translate("MainWindow", "Wave generator"))
        self.label_3.setText(_translate("MainWindow", "t2, ms"))
        self.label_4.setText(_translate("MainWindow", "t3, ms"))
        self.SetWGButton.setText(_translate("MainWindow", "Set parameter"))
        self.label.setText(_translate("MainWindow", "V1, V"))
        self.label_9.setText(_translate("MainWindow", "t1, ms"))
        self.label_2.setText(_translate("MainWindow", "V2, V"))
        self.label_8.setText(_translate("MainWindow", "n_cycl"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Monitor"))
        self.Monitor_Button.setText(_translate("MainWindow", "Monitor ON"))
        self.Set_DAQ_Button.setText(_translate("MainWindow", "Set parameter"))
        self.label_6.setText(_translate("MainWindow", "ch_num"))
        self.label_5.setText(_translate("MainWindow", "num_smpl"))
        self.label_7.setText(_translate("MainWindow", "rate"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Save"))
        self.Rec_Button.setText(_translate("MainWindow", "Record"))
        self.label_11.setText(_translate("MainWindow", "path"))
        self.label_12.setText(_translate("MainWindow", "filename"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_13.setText(_translate("MainWindow", "Monitor"))
        self.label_14.setText(_translate("MainWindow", "ON"))
        self.label_15.setText(_translate("MainWindow", "Record"))
        self.label_16.setText(_translate("MainWindow", "OFF"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Motor"))
        self.DH_Button.setText(_translate("MainWindow", "Define Home"))
        self.MR_Button.setText(_translate("MainWindow", "Move Relative"))
        self.GH_Button.setText(_translate("MainWindow", "Go Home"))
        self.MN_Button.setText(_translate("MainWindow", "Motor ON"))
        self.TP_Button.setText(_translate("MainWindow", "Tell Position"))
        self.MA_Button.setText(_translate("MainWindow", "Move Absolute"))
        self.SentCommand_Buttun.setText(_translate("MainWindow", "Command"))

