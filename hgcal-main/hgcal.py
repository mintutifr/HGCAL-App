#  x,y,z,board_no-board_type-date-time :  7 hole file structure

#import standard programs
import sys, os, glob, csv, re
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
#from subprocess import call, PIPE, Popen


#import user programs
from hgcal_gui import *

global dir_path

# Check the actions to be performed (Button of Menu)
def signals(self):
    check_dir(self)
    # quit action by button or by menu (QUIT)
    self.pushButton_quit.clicked.connect(self.quit)
    self.actionQuit.triggered.connect(self.quit)
    
    # automated inspection action by button or by menu (Automaton Inspection)
    self.pushButton_autoInspection.clicked.connect(self.autoInspection)
    self.actionAutoInspection.triggered.connect(self.autoInspection)

    # mage processing action by button or by menu (Image Processing)
    self.pushButton_imageProcesing.clicked.connect(self.imageProcesing)
    self.actionImageProcesing.triggered.connect(self.imageProcesing)

    # corrected inspection action by button or by menu (Corrected Inspection)
    self.pushButton_correctedInspection.clicked.connect(self.correctedInspection)
    self.actionImageProcesing.triggered.connect(self.correctedInspection)

# Action for Quit
def quit(self):
    QtWidgets.QApplication.quit()

# Check Directory
def check_dir(self):
    global dir_path
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print (dir_path)
    head_tail = os.path.split(dir_path)
    dir_path = head_tail[0]
    print (dir_path)

# Action AutoInspection
def autoInspection(self):
    global dir_path
    print("Automated Inspection")
    cmd = "python " + dir_path + "/automated_inspecton/automated_inspection.py"
    returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
    print('returned value:', returned_value)


# Action Image Processing (CannyEdge)
def imageProcesing(self):
    global dir_path
    path = dir_path + "/image_processing"
    os.chdir(path)
    print (path)
    print("Image Processing")
    cmd = "python MyPyQT.py"
    returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
    print('returned value:', returned_value)

# Action Corrected Inspection
def correctedInspection(self):
    global dir_path
    print("Corrected Inspection")
    cmd = "python " + dir_path + "/corrected_inspection/corrected_inspection.py"
    returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
    print('returned value:', returned_value)
        
# Main function to set all the necessary actions.
def main():
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    #os.environ["QT_SCREEN_SCALE_FACTOR"] = "1"
    #os.environ["QT_SCALE_FACTOR"] = "1.5"
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

    # Handle high resolution displays:
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    try:
        app
    except:
        app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_hgcal()
    ui.setupUi(MainWindow)  
    
    #MainWindow.showMaximized()
    MainWindow.show()

    # call the action routeen
    ui.signals()

    # Exit the application on pressong the close (X) on the screen
    sys.exit(app.exec_())

# Start the application and initiate the GUI
if __name__ == "__main__":
    Ui_MainWindow_hgcal.signals = signals
    Ui_MainWindow_hgcal.quit = quit
    Ui_MainWindow_hgcal.autoInspection = autoInspection
    Ui_MainWindow_hgcal.imageProcesing = imageProcesing
    Ui_MainWindow_hgcal.correctedInspection = correctedInspection
    main()
