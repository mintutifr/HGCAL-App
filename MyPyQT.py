from PyQt5.QtWidgets import QMainWindow, QFileDialog, QFrame, QApplication, QPushButton, QDialog, QGroupBox, \
    QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QWidget
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
import os, cv2, sys
import numpy as np
import pandas as pd
import ROOT as R
import glob
R.gInterpreter.ProcessLine('#include "analyse_data_v07.C"')

class My_main_Window(QDialog):
    def __init__(self):
        super().__init__()
        self.currentImg = 0
        self.title = "GridLayout"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 100

        self.InitWindow()
        self.show()

    def InitWindow(self):
        path = QApplication.applicationDirPath()
        self.setWindowIcon(QtGui.QIcon('main_icon.jpeg'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_button()
        self.create_label()

    def create_button(self):

        Import_Img_button = QPushButton("Import Img", self)
        Import_Img_button.setGeometry(QRect(10, 35, 135, 45))  # (x,y,deltaX,deltaY)
        Import_Img_button.setIcon(QtGui.QIcon("image_icon.jpeg"))
        Import_Img_button.setIconSize(QtCore.QSize(40, 40))
        Import_Img_button.setToolTip("<h2> click here to import the image<h2>")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Import_Img_button.setFont(font)
        Import_Img_button.clicked.connect(self.loadImage)

        Next_Img_Button = QPushButton("Next Image", self)
        Next_Img_Button.setGeometry(QtCore.QRect(10, 90, 135, 45))
        Next_Img_Button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Next_Img_Button.setIcon(QtGui.QIcon("next_Img.jpg"))
        Next_Img_Button.setIconSize(QtCore.QSize(43, 43))
        Next_Img_Button.setToolTip("<h2> click here to select the Next Image<h2>")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Next_Img_Button.setFont(font)
        Next_Img_Button.clicked.connect(self.nextImage)

        Priv_Img_Button = QPushButton(" Priv Image", self)
        Priv_Img_Button.setGeometry(QtCore.QRect(10, 145, 135, 45))
        Priv_Img_Button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Priv_Img_Button.setIcon(QtGui.QIcon("privous_Img.jpeg"))
        Priv_Img_Button.setIconSize(QtCore.QSize(33, 33))
        Priv_Img_Button.setToolTip("<h2> click here to select the Privous Image<h2>")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Priv_Img_Button.setFont(font)
        Priv_Img_Button.clicked.connect(self.preImage)

        Process_Button = QPushButton(" Process Img", self)
        Process_Button.setGeometry(QtCore.QRect(10, 200, 135, 45))
        Process_Button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Process_Button.setIcon(QtGui.QIcon("processing.png"))
        Process_Button.setIconSize(QtCore.QSize(35, 35))
        Process_Button.setToolTip("<h2> click here to process the Image<h2>")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Process_Button.setFont(font)
        Process_Button.clicked.connect(self.Docanny)

        CSV_Button = QPushButton(" Export csv  ", self)
        CSV_Button.setGeometry(QtCore.QRect(10, 255, 135, 45))
        CSV_Button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        CSV_Button.setIcon(QtGui.QIcon("export_csv.png"))
        CSV_Button.setIconSize(QtCore.QSize(35, 40))
        CSV_Button.setToolTip("<h2> click here to Export pixel into the CSV file<h2>")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        CSV_Button.setFont(font)
        CSV_Button.clicked.connect(self.Exportcsv)

        RunInLoop_Button = QPushButton(" Run for All ", self)
        RunInLoop_Button.setGeometry(QtCore.QRect(10, 310, 135, 45))
        RunInLoop_Button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        RunInLoop_Button.setIcon(QtGui.QIcon("loop.jpeg"))
        RunInLoop_Button.setIconSize(QtCore.QSize(35, 43))
        RunInLoop_Button.setToolTip("<h2> click here to Exit the application<h2>")
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        RunInLoop_Button.setFont(font)
        RunInLoop_Button.clicked.connect(self.RunForAll)

    def create_label(self):
        self.labelImgname = QLabel("Image Name")
        self.labelImgname.setMinimumSize(25, 18)
        self.labelImgname.setAlignment(QtCore.Qt.AlignCenter)
        #self.labelImgname.setStyleSheet("background-color:yellow")

        self.labelImg = QLabel("Image Block")
        # layout.addWidget(self.label, 0, 0, 1, 2)
        self.labelImg.setMinimumSize(250, 187)
        self.labelImg.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImg.setStyleSheet("background-color:yellow")

        self.labelcan = QLabel("CannyEdge Block")
        # layout.addWidget(self.label, 0, 0, 1, 2)
        self.labelcan.setMinimumSize(250, 187)
        self.labelcan.setAlignment(QtCore.Qt.AlignCenter)
        self.labelcan.setStyleSheet("background-color:green")

        self.labelcent = QLabel("Centroid finder Block")
        # layout.addWidget(self.label, 0, 0, 1, 2)
        self.labelcent.setMinimumSize(250, 187)
        self.labelcent.setAlignment(QtCore.Qt.AlignCenter)
        self.labelcent.setStyleSheet("background-color:yellow")


        grilayout = QGridLayout()
        grilayout.addWidget(self.labelImgname, 1, 0)
        grilayout.addWidget(self.labelImg, 2, 0)  # , 1, 2)#(self.labelImg, 0, 1)
        grilayout.addWidget(self.labelcan, 3, 0)
        grilayout.addWidget(self.labelcent, 2, 1)

        self.groupbox = QGroupBox()
        self.groupbox.setLayout(grilayout)

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)
        vbox.setContentsMargins(150, 30, -10, 30)
        QDialog.setLayout(self, vbox)
        QDialog.setGeometry(self, 500, 30, 400, 200)

    def Print(slef):
        print("Hello world")

    def CloseMe(self):
        sys.exit()

    def loadImage(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Select Image', '', 'Image Files (*.png *.jpg)')
        self.labelImg.setText("Image Type:" + filename)
        #print(filename)
        if filename:
            pixmap = QtGui.QPixmap(filename).scaled(self.labelImg.size(),
                                                    QtCore.Qt.KeepAspectRatio)
            if pixmap.isNull():
                return
            self.labelImg.setPixmap(pixmap)
            self.labelImgname.setText(filename.split("/")[-1])
            dirpath = os.path.dirname(filename)
            if not os.path.exists(dirpath+"/CSV"):
                os.mkdir(dirpath+"/CSV")
                #os.mkdir(dirpath+"/CSV/csv_Focused")  # Swich this on when working in python in windoes
            if not os.path.exists(dirpath+"/canny"):
                os.mkdir(dirpath + "/canny")
                #os.mkdir(dirpath + "/canny/canny_Focused") # Swich this on when working in python in windoes
            if not os.path.isdir(dirpath+"/Centroid/"):
                os.mkdir(dirpath+"/Centroid")
            print(dirpath)
            self.fileList = []
            for f in os.listdir(dirpath):
                fpath = os.path.join(dirpath, f)
                if os.path.isfile(fpath) and f.endswith(('.png', '.jpg')):
                    self.fileList.append(fpath)
            self.fileList.sort()
            print(self.fileList)
            # self.dirIterator = iter(self.fileList)
            # print(filename)
            # print(next(self.dirIterator))
            for i in range(0, len(self.fileList)):
                #print(self.fileList[i])
                # cycle through the iterator until the current file is found
                # print(filename)
                if self.fileList[i] == filename:
                    self.currentImg = i
                    break

    def nextImage(self):
        # ensure that the file list has not been cleared due to missing files
        if self.fileList:
            self.currentImg = self.currentImg + 1
            try:
                filename = self.fileList[self.currentImg]
                pixmap = QtGui.QPixmap(filename).scaled(self.labelImg.size(),
                                                        QtCore.Qt.KeepAspectRatio)
                if pixmap.isNull():
                    # the file is not a valid image, remove it from the list
                    # and try to load the next one
                    self.fileList.remove(filename)
                    self.nextImage()
                else:
                    self.labelImg.setPixmap(pixmap)
                    self.labelImgname.setText(filename.split("/")[-1])
                    self.Docanny()
            except:
                self.currentImg = -1
                self.nextImage()
        else:
            # no file list found, load an image
            self.loadImage()

    def preImage(self):
        # ensure that the file list has not been cleared due to missing files
        if(self.fileList and (self.currentImg)!=0):
            self.currentImg = self.currentImg - 1
            #print(self.fileList[self.currentImg], self.currentImg)
            try:
                filename = self.fileList[self.currentImg]
                pixmap = QtGui.QPixmap(filename).scaled(self.labelImg.size(),
                                                        QtCore.Qt.KeepAspectRatio)
                if pixmap.isNull():
                    # the file is not a valid image, remove it from the list
                    # and try to load the next one
                    self.fileList.remove(filename)
                    self.preImage()
                else:
                    self.labelImg.setPixmap(pixmap)
                    self.labelImgname.setText(filename.split("/")[-1])
                    self.Docanny()
            except:
                sys.exit(0)
        else:
            self.currentImg = len(self.fileList)
            #print(self.fileList[self.currentImg-1],self.currentImg)
            self.preImage()
            # no file list found, load an image
            #self.loadImage()

    def Docanny(self):
        try:
            image = cv2.imread(self.fileList[self.currentImg])
            image = cv2.blur(image, (5, 5),1.4)
            kernel = np.ones((3, 3), np.uint8)
            img_erosion = cv2.erode(image, kernel, iterations=6)
            (thresh, blackAndWhiteImage) = cv2.threshold(img_erosion, 200, 255, cv2.THRESH_BINARY)
            self.tight = cv2.Canny(blackAndWhiteImage, 240, 255)
            self.coordinates = np.argwhere(self.tight == 255)
            self.y, self.x = zip(*self.coordinates)
            self.Draw_Image(self.tight)

            cv2.imwrite(os.path.dirname(self.fileList[self.currentImg])+"/canny/canny_"+self.fileList[self.currentImg].split(".")[0].split("/")[-1] + ".jpeg",self.tight)
            print(os.path.dirname(self.fileList[self.currentImg])+"/canny/canny_"+self.fileList[self.currentImg].split(".")[0].split("/")[-1] + ".jpeg")
            #print(  self.fileList[self.currentImg].split(".")[0].split("/")[-1] )



        except Exception as e:
            print(e)
            print("Please select the first image first something wrong in Docanny fun ")

    def Draw_Image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_to_qt(cv_img)
        #self.coordinate_Display.setPixmap(qt_img)
        pixmap = QtGui.QPixmap(qt_img).scaled(self.labelcan.size(),
                                                QtCore.Qt.KeepAspectRatio)
        if pixmap.isNull():
            print("pixal map is not properly done")
        else:
            self.labelcan.setPixmap(pixmap)


    def convert_cv_to_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        return QPixmap.fromImage(convert_to_Qt_format)


    def Exportcsv(self):
        try:
            self.Docanny()
            print( "csv file ",(self.fileList[self.currentImg])+"/CSV/csv_"+self.fileList[self.currentImg].split(".")[0].split("/")[-1] + ".csv" ,"exported")
            #pd.DataFrame(self.coordinates).to_csv((self.fileList[self.currentImg].split("."))[0]+".csv", index=False,header=['y_coord', 'x_coord'])
            pd.DataFrame(self.coordinates).to_csv(os.path.dirname(self.fileList[self.currentImg])+"/CSV/csv_"+self.fileList[self.currentImg].split(".")[0].split("/")[-1] + ".csv", index=False,header=['y_coord', 'x_coord'])

            self.RunCentriodFinder(os.path.dirname(self.fileList[self.currentImg])+"/CSV/","csv_"+self.fileList[self.currentImg].split(".")[0].split("/")[-1])
            #slopanderror = np.zeros(13)
            #R.analyse_data_v07(os.path.dirname(self.fileList[self.currentImg])+"/CSV/","csv_"+self.fileList[self.currentImg].split(".")[0].split("/")[-1], slopanderror)
            #folder_path = os.path.dirname(self.fileList[self.currentImg])+"/Centroid/"
            #file_type = '*png'
            #files = glob.glob(folder_path + file_type)
            #max_file = max(files, key=os.path.getctime)
            #print (max_file)
            #if max_file:
             #   pixmap = QtGui.QPixmap(max_file).scaled(self.labelcent.size(),
             #                                           QtCore.Qt.KeepAspectRatio)
              #  if pixmap.isNull():
               #     return
                #self.labelcent.setPixmap(pixmap)
                #self.labelImgname.setText(max_file.split("/")[-1])
        except Exception as e:
            print(e)
            print("Please select the first image first something wrong in Export csv fun ")

    def RunCentriodFinder(self,dir,imagename):
        try:
            slopanderror = np.zeros(13)
            R.analyse_data_v07(dir,imagename, slopanderror)
            folder_path = dir + "../Centroid/"
            file_type = '*png'
            files = glob.glob(folder_path + file_type)
            max_file = max(files, key=os.path.getctime)
            print(max_file)
            if max_file:
                pixmap = QtGui.QPixmap(max_file).scaled(self.labelcent.size(),
                                                    QtCore.Qt.KeepAspectRatio)
                if pixmap.isNull():
                    return
                self.labelcent.setPixmap(pixmap)
                self.labelImgname.setText(max_file.split("/")[-1])
        except Exception as e:
            print(e)
            print("Please select the first image first something wrong in RunCentriodFinder")

    def RunForAll(self):
        try:
            for image_num in range(0,len(self.fileList)):
                self.currentImg = image_num
                print(self.currentImg)
                self.Docanny()
                self.Exportcsv()
        except:
            print("Please select the first image first")

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = My_main_Window()
    sys.exit(App.exec())
