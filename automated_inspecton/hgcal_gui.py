# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HGCAL-App/automated_inspecton/hgcal_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_hgcal(object):
    def setupUi(self, MainWindow_hgcal):
        MainWindow_hgcal.setObjectName("MainWindow_hgcal")
        MainWindow_hgcal.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow_hgcal.resize(600, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow_hgcal.sizePolicy().hasHeightForWidth())
        MainWindow_hgcal.setSizePolicy(sizePolicy)
        MainWindow_hgcal.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow_hgcal.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow_hgcal.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow_hgcal.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow_hgcal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 586, 267))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_title = QtWidgets.QVBoxLayout()
        self.verticalLayout_title.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_title.setObjectName("verticalLayout_title")
        self.label_index_text = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_index_text.sizePolicy().hasHeightForWidth())
        self.label_index_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_index_text.setFont(font)
        self.label_index_text.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_index_text.setObjectName("label_index_text")
        self.verticalLayout_title.addWidget(self.label_index_text)
        self.gridLayout_2.addLayout(self.verticalLayout_title, 0, 0, 1, 1)
        self.horizontalLayout_buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_buttons.setSpacing(1)
        self.horizontalLayout_buttons.setObjectName("horizontalLayout_buttons")
        self.pushButton_quit = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_quit.sizePolicy().hasHeightForWidth())
        self.pushButton_quit.setSizePolicy(sizePolicy)
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.horizontalLayout_buttons.addWidget(self.pushButton_quit)
        self.pushButton_autoInspection = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_autoInspection.sizePolicy().hasHeightForWidth())
        self.pushButton_autoInspection.setSizePolicy(sizePolicy)
        self.pushButton_autoInspection.setObjectName("pushButton_autoInspection")
        self.horizontalLayout_buttons.addWidget(self.pushButton_autoInspection)
        self.pushButton_cannyEdge = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cannyEdge.sizePolicy().hasHeightForWidth())
        self.pushButton_cannyEdge.setSizePolicy(sizePolicy)
        self.pushButton_cannyEdge.setObjectName("pushButton_cannyEdge")
        self.horizontalLayout_buttons.addWidget(self.pushButton_cannyEdge)
        self.pushButton_OffsetCorrection = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_OffsetCorrection.sizePolicy().hasHeightForWidth())
        self.pushButton_OffsetCorrection.setSizePolicy(sizePolicy)
        self.pushButton_OffsetCorrection.setObjectName("pushButton_OffsetCorrection")
        self.horizontalLayout_buttons.addWidget(self.pushButton_OffsetCorrection)
        self.gridLayout_2.addLayout(self.horizontalLayout_buttons, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow_hgcal.setCentralWidget(self.centralwidget)
        self.menubar_file = QtWidgets.QMenuBar(MainWindow_hgcal)
        self.menubar_file.setGeometry(QtCore.QRect(0, 0, 600, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar_file.sizePolicy().hasHeightForWidth())
        self.menubar_file.setSizePolicy(sizePolicy)
        self.menubar_file.setObjectName("menubar_file")
        self.menuAction = QtWidgets.QMenu(self.menubar_file)
        self.menuAction.setObjectName("menuAction")
        MainWindow_hgcal.setMenuBar(self.menubar_file)
        self.actionAutoInspection = QtWidgets.QAction(MainWindow_hgcal)
        self.actionAutoInspection.setObjectName("actionAutoInspection")
        self.actionCannyEdge = QtWidgets.QAction(MainWindow_hgcal)
        self.actionCannyEdge.setObjectName("actionCannyEdge")
        self.actionQuit = QtWidgets.QAction(MainWindow_hgcal)
        self.actionQuit.setObjectName("actionQuit")
        self.menuAction.addAction(self.actionAutoInspection)
        self.menuAction.addAction(self.actionCannyEdge)
        self.menuAction.addAction(self.actionQuit)
        self.menubar_file.addAction(self.menuAction.menuAction())

        self.retranslateUi(MainWindow_hgcal)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_hgcal)

    def retranslateUi(self, MainWindow_hgcal):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_hgcal.setWindowTitle(_translate("MainWindow_hgcal", "HGCAL silicon module"))
        self.label_index_text.setText(_translate("MainWindow_hgcal", "HGCAL Silicon Module"))
        self.pushButton_quit.setToolTip(_translate("MainWindow_hgcal", "<html><head/><body><p>Quit the Program</p></body></html>"))
        self.pushButton_quit.setText(_translate("MainWindow_hgcal", "Quit"))
        self.pushButton_autoInspection.setToolTip(_translate("MainWindow_hgcal", "<html><head/><body><p>This Progem accepts 7 hole coordinates and executes Pass0</p></body></html>"))
        self.pushButton_autoInspection.setText(_translate("MainWindow_hgcal", "Automated Inspection"))
        self.pushButton_cannyEdge.setToolTip(_translate("MainWindow_hgcal", "<html><head/><body><p>This application can be used to plot the edges in a given image and also export them.</p></body></html>"))
        self.pushButton_cannyEdge.setText(_translate("MainWindow_hgcal", "Canny Edge Detector"))
        self.pushButton_OffsetCorrection.setText(_translate("MainWindow_hgcal", "Correction"))
        self.menuAction.setTitle(_translate("MainWindow_hgcal", "Action"))
        self.actionAutoInspection.setText(_translate("MainWindow_hgcal", "Automated Inspection"))
        self.actionCannyEdge.setText(_translate("MainWindow_hgcal", "Canny Edge Detector"))
        self.actionQuit.setText(_translate("MainWindow_hgcal", "Quit"))
