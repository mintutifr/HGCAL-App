# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'corrected_inspection_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_MiniGrantry_pass3(object):
    def setupUi(self, MainWindow_MiniGrantry_pass3):
        MainWindow_MiniGrantry_pass3.setObjectName("MainWindow_MiniGrantry_pass3")
        MainWindow_MiniGrantry_pass3.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow_MiniGrantry_pass3.resize(791, 469)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow_MiniGrantry_pass3.sizePolicy().hasHeightForWidth())
        MainWindow_MiniGrantry_pass3.setSizePolicy(sizePolicy)
        MainWindow_MiniGrantry_pass3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow_MiniGrantry_pass3.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow_MiniGrantry_pass3.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow_MiniGrantry_pass3.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow_MiniGrantry_pass3)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 777, 436))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Titile = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_Titile.setFont(font)
        self.label_Titile.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_Titile.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Titile.setWordWrap(False)
        self.label_Titile.setObjectName("label_Titile")
        self.verticalLayout.addWidget(self.label_Titile)
        self.label_description = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_description.setFont(font)
        self.label_description.setWordWrap(True)
        self.label_description.setObjectName("label_description")
        self.verticalLayout.addWidget(self.label_description)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_date = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date.sizePolicy().hasHeightForWidth())
        self.label_date.setSizePolicy(sizePolicy)
        self.label_date.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")
        self.horizontalLayout.addWidget(self.label_date)
        self.lineEdit_date = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_date.sizePolicy().hasHeightForWidth())
        self.lineEdit_date.setSizePolicy(sizePolicy)
        self.lineEdit_date.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_date.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_date.setFont(font)
        self.lineEdit_date.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.horizontalLayout.addWidget(self.lineEdit_date)
        self.label_time = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_time.sizePolicy().hasHeightForWidth())
        self.label_time.setSizePolicy(sizePolicy)
        self.label_time.setMaximumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.horizontalLayout.addWidget(self.label_time)
        self.lineEdit_time = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_time.sizePolicy().hasHeightForWidth())
        self.lineEdit_time.setSizePolicy(sizePolicy)
        self.lineEdit_time.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_time.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_time.setFont(font)
        self.lineEdit_time.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.horizontalLayout.addWidget(self.lineEdit_time)
        self.label_date_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_date_3.sizePolicy().hasHeightForWidth())
        self.label_date_3.setSizePolicy(sizePolicy)
        self.label_date_3.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_date_3.setFont(font)
        self.label_date_3.setObjectName("label_date_3")
        self.horizontalLayout.addWidget(self.label_date_3)
        self.lineEdit_btype = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_btype.sizePolicy().hasHeightForWidth())
        self.lineEdit_btype.setSizePolicy(sizePolicy)
        self.lineEdit_btype.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_btype.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_btype.setFont(font)
        self.lineEdit_btype.setObjectName("lineEdit_btype")
        self.horizontalLayout.addWidget(self.lineEdit_btype)
        self.label_board_no = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_board_no.sizePolicy().hasHeightForWidth())
        self.label_board_no.setSizePolicy(sizePolicy)
        self.label_board_no.setMaximumSize(QtCore.QSize(75, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_board_no.setFont(font)
        self.label_board_no.setObjectName("label_board_no")
        self.horizontalLayout.addWidget(self.label_board_no)
        self.lineEdit_board_no = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_board_no.sizePolicy().hasHeightForWidth())
        self.lineEdit_board_no.setSizePolicy(sizePolicy)
        self.lineEdit_board_no.setMinimumSize(QtCore.QSize(50, 30))
        self.lineEdit_board_no.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_board_no.setFont(font)
        self.lineEdit_board_no.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_board_no.setToolTipDuration(-1)
        self.lineEdit_board_no.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_board_no.setInputMask("00000")
        self.lineEdit_board_no.setText("")
        self.lineEdit_board_no.setMaxLength(5)
        self.lineEdit_board_no.setCursorPosition(5)
        self.lineEdit_board_no.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_board_no.setObjectName("lineEdit_board_no")
        self.horizontalLayout.addWidget(self.lineEdit_board_no)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_CSV_pass3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_CSV_pass3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_CSV_pass3.sizePolicy().hasHeightForWidth())
        self.label_CSV_pass3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_CSV_pass3.setFont(font)
        self.label_CSV_pass3.setObjectName("label_CSV_pass3")
        self.verticalLayout_4.addWidget(self.label_CSV_pass3)
        self.label_MC5_pass3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_MC5_pass3.sizePolicy().hasHeightForWidth())
        self.label_MC5_pass3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_MC5_pass3.setFont(font)
        self.label_MC5_pass3.setScaledContents(False)
        self.label_MC5_pass3.setObjectName("label_MC5_pass3")
        self.verticalLayout_4.addWidget(self.label_MC5_pass3)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_output_CSV_pass3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_output_CSV_pass3.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_output_CSV_pass3.setFont(font)
        self.label_output_CSV_pass3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_output_CSV_pass3.setObjectName("label_output_CSV_pass3")
        self.verticalLayout_5.addWidget(self.label_output_CSV_pass3)
        self.label_output_MC5_pass3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_output_MC5_pass3.sizePolicy().hasHeightForWidth())
        self.label_output_MC5_pass3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_output_MC5_pass3.setFont(font)
        self.label_output_MC5_pass3.setObjectName("label_output_MC5_pass3")
        self.verticalLayout_5.addWidget(self.label_output_MC5_pass3)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_5)
        self.gridLayout_4.addLayout(self.formLayout, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_quit = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_quit.sizePolicy().hasHeightForWidth())
        self.pushButton_quit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_quit.setFont(font)
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.horizontalLayout_2.addWidget(self.pushButton_quit)
        self.pushButton_reset_pass3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_reset_pass3.sizePolicy().hasHeightForWidth())
        self.pushButton_reset_pass3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_reset_pass3.setFont(font)
        self.pushButton_reset_pass3.setObjectName("pushButton_reset_pass3")
        self.horizontalLayout_2.addWidget(self.pushButton_reset_pass3)
        self.pushButton_Pass3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Pass3.sizePolicy().hasHeightForWidth())
        self.pushButton_Pass3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Pass3.setFont(font)
        self.pushButton_Pass3.setObjectName("pushButton_Pass3")
        self.horizontalLayout_2.addWidget(self.pushButton_Pass3)
        self.pushButton_transfer = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_transfer.sizePolicy().hasHeightForWidth())
        self.pushButton_transfer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_transfer.setFont(font)
        self.pushButton_transfer.setObjectName("pushButton_transfer")
        self.horizontalLayout_2.addWidget(self.pushButton_transfer)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 8, 0, 1, 1)
        self.lineEdit_destinationPath = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_destinationPath.setFont(font)
        self.lineEdit_destinationPath.setObjectName("lineEdit_destinationPath")
        self.gridLayout_4.addWidget(self.lineEdit_destinationPath, 7, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_Finish_Pass = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Finish_Pass.setFont(font)
        self.label_Finish_Pass.setText("")
        self.label_Finish_Pass.setScaledContents(False)
        self.label_Finish_Pass.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Finish_Pass.setObjectName("label_Finish_Pass")
        self.verticalLayout_3.addWidget(self.label_Finish_Pass)
        self.label_server_details = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_server_details.setFont(font)
        self.label_server_details.setObjectName("label_server_details")
        self.verticalLayout_3.addWidget(self.label_server_details)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 5, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_pass2_csv = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pass2_csv.sizePolicy().hasHeightForWidth())
        self.label_pass2_csv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_pass2_csv.setFont(font)
        self.label_pass2_csv.setObjectName("label_pass2_csv")
        self.verticalLayout_2.addWidget(self.label_pass2_csv)
        self.label_gerber_75_pass1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_gerber_75_pass1.sizePolicy().hasHeightForWidth())
        self.label_gerber_75_pass1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_gerber_75_pass1.setFont(font)
        self.label_gerber_75_pass1.setObjectName("label_gerber_75_pass1")
        self.verticalLayout_2.addWidget(self.label_gerber_75_pass1)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 2, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_input_pass2_csv = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_input_pass2_csv.setFont(font)
        self.label_input_pass2_csv.setObjectName("label_input_pass2_csv")
        self.verticalLayout_6.addWidget(self.label_input_pass2_csv)
        self.label_input_gerber_75 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_input_gerber_75.setFont(font)
        self.label_input_gerber_75.setObjectName("label_input_gerber_75")
        self.verticalLayout_6.addWidget(self.label_input_gerber_75)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 1, 2, 1)
        self.pushButton_get_CSV = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_get_CSV.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_get_CSV.sizePolicy().hasHeightForWidth())
        self.pushButton_get_CSV.setSizePolicy(sizePolicy)
        self.pushButton_get_CSV.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_get_CSV.setObjectName("pushButton_get_CSV")
        self.gridLayout.addWidget(self.pushButton_get_CSV, 0, 2, 1, 1)
        self.pushButton_get_gerber = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_get_gerber.sizePolicy().hasHeightForWidth())
        self.pushButton_get_gerber.setSizePolicy(sizePolicy)
        self.pushButton_get_gerber.setAutoDefault(False)
        self.pushButton_get_gerber.setObjectName("pushButton_get_gerber")
        self.gridLayout.addWidget(self.pushButton_get_gerber, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_user = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_user.sizePolicy().hasHeightForWidth())
        self.lineEdit_user.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.horizontalLayout_7.addWidget(self.lineEdit_user)
        self.lineEdit_server = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_server.sizePolicy().hasHeightForWidth())
        self.lineEdit_server.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_server.setFont(font)
        self.lineEdit_server.setText("")
        self.lineEdit_server.setObjectName("lineEdit_server")
        self.horizontalLayout_7.addWidget(self.lineEdit_server)
        self.lineEdit_password = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_password.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_7.addWidget(self.lineEdit_password)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 6, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget_pass2_coordinates = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_pass2_coordinates.sizePolicy().hasHeightForWidth())
        self.tableWidget_pass2_coordinates.setSizePolicy(sizePolicy)
        self.tableWidget_pass2_coordinates.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tableWidget_pass2_coordinates.setFont(font)
        self.tableWidget_pass2_coordinates.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.tableWidget_pass2_coordinates.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tableWidget_pass2_coordinates.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tableWidget_pass2_coordinates.setToolTip("")
        self.tableWidget_pass2_coordinates.setAutoFillBackground(False)
        self.tableWidget_pass2_coordinates.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tableWidget_pass2_coordinates.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget_pass2_coordinates.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_pass2_coordinates.setLineWidth(0)
        self.tableWidget_pass2_coordinates.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_pass2_coordinates.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_pass2_coordinates.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_pass2_coordinates.setAutoScroll(True)
        self.tableWidget_pass2_coordinates.setAlternatingRowColors(True)
        self.tableWidget_pass2_coordinates.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_pass2_coordinates.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_pass2_coordinates.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget_pass2_coordinates.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget_pass2_coordinates.setShowGrid(True)
        self.tableWidget_pass2_coordinates.setWordWrap(True)
        self.tableWidget_pass2_coordinates.setCornerButtonEnabled(True)
        self.tableWidget_pass2_coordinates.setRowCount(0)
        self.tableWidget_pass2_coordinates.setColumnCount(5)
        self.tableWidget_pass2_coordinates.setObjectName("tableWidget_pass2_coordinates")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_pass2_coordinates.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_pass2_coordinates.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_pass2_coordinates.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_pass2_coordinates.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_pass2_coordinates.setHorizontalHeaderItem(4, item)
        self.tableWidget_pass2_coordinates.horizontalHeader().setVisible(True)
        self.tableWidget_pass2_coordinates.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_pass2_coordinates.horizontalHeader().setDefaultSectionSize(142)
        self.tableWidget_pass2_coordinates.horizontalHeader().setHighlightSections(True)
        self.tableWidget_pass2_coordinates.horizontalHeader().setMinimumSectionSize(101)
        self.tableWidget_pass2_coordinates.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_pass2_coordinates.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_pass2_coordinates.verticalHeader().setVisible(False)
        self.tableWidget_pass2_coordinates.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_pass2_coordinates.verticalHeader().setDefaultSectionSize(26)
        self.tableWidget_pass2_coordinates.verticalHeader().setHighlightSections(False)
        self.tableWidget_pass2_coordinates.verticalHeader().setMinimumSectionSize(16)
        self.tableWidget_pass2_coordinates.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_pass2_coordinates.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.tableWidget_pass2_coordinates, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_4.addItem(spacerItem, 9, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow_MiniGrantry_pass3.setCentralWidget(self.centralwidget)
        self.menubar_file = QtWidgets.QMenuBar(MainWindow_MiniGrantry_pass3)
        self.menubar_file.setGeometry(QtCore.QRect(0, 0, 791, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar_file.sizePolicy().hasHeightForWidth())
        self.menubar_file.setSizePolicy(sizePolicy)
        self.menubar_file.setObjectName("menubar_file")
        self.menuFile = QtWidgets.QMenu(self.menubar_file)
        self.menuFile.setObjectName("menuFile")
        MainWindow_MiniGrantry_pass3.setMenuBar(self.menubar_file)
        self.actionsave = QtWidgets.QAction(MainWindow_MiniGrantry_pass3)
        self.actionsave.setObjectName("actionsave")
        self.actionreset = QtWidgets.QAction(MainWindow_MiniGrantry_pass3)
        self.actionreset.setObjectName("actionreset")
        self.actiontransfer = QtWidgets.QAction(MainWindow_MiniGrantry_pass3)
        self.actiontransfer.setObjectName("actiontransfer")
        self.actionquit = QtWidgets.QAction(MainWindow_MiniGrantry_pass3)
        self.actionquit.setObjectName("actionquit")
        self.action_get_CSV = QtWidgets.QAction(MainWindow_MiniGrantry_pass3)
        self.action_get_CSV.setObjectName("action_get_CSV")
        self.action_get_gerber = QtWidgets.QAction(MainWindow_MiniGrantry_pass3)
        self.action_get_gerber.setObjectName("action_get_gerber")
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionreset)
        self.menuFile.addAction(self.actiontransfer)
        self.menuFile.addAction(self.actionquit)
        self.menuFile.addAction(self.action_get_CSV)
        self.menuFile.addAction(self.action_get_gerber)
        self.menubar_file.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow_MiniGrantry_pass3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_MiniGrantry_pass3)

    def retranslateUi(self, MainWindow_MiniGrantry_pass3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_MiniGrantry_pass3.setWindowTitle(_translate("MainWindow_MiniGrantry_pass3", "Corrected Inspection HGCAL silicon module"))
        self.label_Titile.setText(_translate("MainWindow_MiniGrantry_pass3", "MiniGantry Pass3"))
        self.label_description.setText(_translate("MainWindow_MiniGrantry_pass3", "1) Accept the corrected hole values from Pass 2 using immage processing  algorithm"))
        self.label.setText(_translate("MainWindow_MiniGrantry_pass3", "2) Generate Pass3 CSV and Pass3  MC5 file using the above mentioned input file"))
        self.label_date.setText(_translate("MainWindow_MiniGrantry_pass3", "Date:"))
        self.label_time.setText(_translate("MainWindow_MiniGrantry_pass3", "Time:"))
        self.label_date_3.setText(_translate("MainWindow_MiniGrantry_pass3", "Board Type:"))
        self.label_board_no.setText(_translate("MainWindow_MiniGrantry_pass3", "Board No.:"))
        self.lineEdit_board_no.setToolTip(_translate("MainWindow_MiniGrantry_pass3", "Insert Boar Number"))
        self.lineEdit_board_no.setPlaceholderText(_translate("MainWindow_MiniGrantry_pass3", "XXXXX"))
        self.label_CSV_pass3.setText(_translate("MainWindow_MiniGrantry_pass3", "Output CSV Pass3 :"))
        self.label_MC5_pass3.setText(_translate("MainWindow_MiniGrantry_pass3", "Output MC5 Pass3:"))
        self.label_output_CSV_pass3.setText(_translate("MainWindow_MiniGrantry_pass3", "CSV pass3 File"))
        self.label_output_MC5_pass3.setText(_translate("MainWindow_MiniGrantry_pass3", "MC5 pass3 File"))
        self.pushButton_quit.setText(_translate("MainWindow_MiniGrantry_pass3", "Quit"))
        self.pushButton_reset_pass3.setText(_translate("MainWindow_MiniGrantry_pass3", "Reset"))
        self.pushButton_Pass3.setText(_translate("MainWindow_MiniGrantry_pass3", "Save"))
        self.pushButton_transfer.setText(_translate("MainWindow_MiniGrantry_pass3", "Transfer"))
        self.lineEdit_destinationPath.setPlaceholderText(_translate("MainWindow_MiniGrantry_pass3", "Destination Path"))
        self.label_server_details.setText(_translate("MainWindow_MiniGrantry_pass3", "Server Details"))
        self.label_pass2_csv.setText(_translate("MainWindow_MiniGrantry_pass3", "Input Pass2 CSV file:"))
        self.label_gerber_75_pass1.setText(_translate("MainWindow_MiniGrantry_pass3", "Input gerber 75 :"))
        self.label_input_pass2_csv.setText(_translate("MainWindow_MiniGrantry_pass3", "Input Pass2 CSV File"))
        self.label_input_gerber_75.setText(_translate("MainWindow_MiniGrantry_pass3", "Input 75 hole gerber file"))
        self.pushButton_get_CSV.setText(_translate("MainWindow_MiniGrantry_pass3", "Select CSV File"))
        self.pushButton_get_gerber.setText(_translate("MainWindow_MiniGrantry_pass3", "Select Gerber File"))
        self.lineEdit_user.setPlaceholderText(_translate("MainWindow_MiniGrantry_pass3", "User on Remote Server"))
        self.lineEdit_server.setPlaceholderText(_translate("MainWindow_MiniGrantry_pass3", "Remote Server IP"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow_MiniGrantry_pass3", "User Password"))
        self.tableWidget_pass2_coordinates.setSortingEnabled(False)
        item = self.tableWidget_pass2_coordinates.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_MiniGrantry_pass3", "Sr._No"))
        item = self.tableWidget_pass2_coordinates.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow_MiniGrantry_pass3", "Hole_Number"))
        item = self.tableWidget_pass2_coordinates.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow_MiniGrantry_pass3", "X-Coordinate(mm)"))
        item = self.tableWidget_pass2_coordinates.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow_MiniGrantry_pass3", "Y-Coordinate(mm)"))
        item = self.tableWidget_pass2_coordinates.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow_MiniGrantry_pass3", "Z-Coordinate(mm)"))
        self.menuFile.setTitle(_translate("MainWindow_MiniGrantry_pass3", "File"))
        self.actionsave.setText(_translate("MainWindow_MiniGrantry_pass3", "save"))
        self.actionsave.setShortcut(_translate("MainWindow_MiniGrantry_pass3", "Ctrl+S"))
        self.actionreset.setText(_translate("MainWindow_MiniGrantry_pass3", "reset"))
        self.actionreset.setShortcut(_translate("MainWindow_MiniGrantry_pass3", "Ctrl+R"))
        self.actiontransfer.setText(_translate("MainWindow_MiniGrantry_pass3", "transfer"))
        self.actiontransfer.setShortcut(_translate("MainWindow_MiniGrantry_pass3", "Ctrl+T"))
        self.actionquit.setText(_translate("MainWindow_MiniGrantry_pass3", "quit"))
        self.actionquit.setShortcut(_translate("MainWindow_MiniGrantry_pass3", "Ctrl+Q"))
        self.action_get_CSV.setText(_translate("MainWindow_MiniGrantry_pass3", "Get CSV"))
        self.action_get_CSV.setShortcut(_translate("MainWindow_MiniGrantry_pass3", "Ctrl+C"))
        self.action_get_gerber.setText(_translate("MainWindow_MiniGrantry_pass3", "GetGerber"))
        self.action_get_gerber.setShortcut(_translate("MainWindow_MiniGrantry_pass3", "Ctrl+G"))