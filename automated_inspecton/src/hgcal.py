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

# Check the actions to be performed (Button of Menu)
def signals(self):

    # quit action by button or by menu (QUIT)
    self.pushButton_quit.clicked.connect(self.quit)
    self.actionQuit.triggered.connect(self.quit)
    
    # automation action by button or by menu (Automaton Inspection)
    self.pushButton_autoInspection.clicked.connect(self.autoInspection)
    self.actionAutoInspection.triggered.connect(self.autoInspection)

    # canny edge detector action by button or by menu (Canny Edge Detector)
    self.pushButton_cannyEdge.clicked.connect(self.cannyEdge)
    self.actionCannyEdge.triggered.connect(self.cannyEdge)

# Action for Quit
def quit(self):
    QtWidgets.QApplication.quit()

# Action AutoInspection
def autoInspection(self):
    print("Auto Inspection")
    cmd = "python3.8 automated_inspection.py"
    returned_value = subprocess.call(cmd, shell=True)  # returns the exit code in unix
    print('returned value:', returned_value)


# Action CannyEdge 
def cannyEdge(self):
    print("Canny Edge Detector")
        
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
    Ui_MainWindow_hgcal.cannyEdge = cannyEdge
    main()
