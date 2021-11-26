#  x,y,z,board_no-board_type-date-time : Pass2 file structure

#import standard programs
import sys, os, glob, csv, re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
from subprocess import call, PIPE, Popen
from shutil import copyfile
import pathlib
from functools import partial
from array import array

#import user programs
from corrected_inspection_gui import *
import hole_offset_correction 
import mc5file_genrater_final_with_XYZ

# Declar Global variables
global dir_path
global pathPass2CSV
global pathPass3CSV
global pathPass3MC5
global inputGerber75
global dateStr 
global btype
global bno
global srno
global flag


# Check the actions to be performed (Button of Menu)
def signals(self):
    check_dir(self)
    resetPass3(self) # Reset before we begain

    # quit action by button or by menu (QUIT)
    self.pushButton_quit.clicked.connect(self.quit)
    self.actionquit.triggered.connect(self.quit)
    
    # Reset action by button or by menu (RESET)
    self.pushButton_reset_pass3.clicked.connect(self.resetPass3)
    self.actionreset.triggered.connect(self.resetPass3)

    # Perform action to generate the Offset file and MC5 file (SAVE)
    self.pushButton_Pass3.clicked.connect(self.pass3)
    self.actionsave.triggered.connect(self.pass3)

    # Perform transfer action by button or by menu (TRANSFER)
    self.pushButton_transfer.clicked.connect(self.transfer)
    self.actiontransfer.triggered.connect(self.transfer)

    self.pushButton_get_CSV.clicked.connect(partial(self.file_handler,'csv'))
    self.action_get_CSV.triggered.connect(partial(self.file_handler,'csv'))
    self.pushButton_get_gerber.clicked.connect(partial(self.file_handler, 'gerber'))
    self.action_get_gerber.triggered.connect(partial(self.file_handler,'gerber'))


def file_handler(self, fileType):
    global inputGerber75 
    global pathPass2CSV
    global flag
    fileName = self.open_file_dialog_box() 
    if fileName != "":
        if fileType == "csv":
            self.label_input_pass2_csv.setText(fileName)
            pathPass2CSV = fileName
            # Read Pass2 CSV and display on the table.
            displayTable(self, pathPass2CSV)
            flag = flag+1
        elif fileType == "gerber":
            self.label_input_gerber_75.setText(fileName)
            inputGerber75 = fileName
            flag = flag+1
        else:
            self.label_input_pass2_csv.setText("Input Pass2 CSV File")
            self.label_input_gerber_75.setText("Input 75 hole gerber file")


        if flag == 2:
            self.pushButton_Pass3.setEnabled(True)
            self.actionsave.setEnabled(True)

def open_file_dialog_box(self):
    filename = QFileDialog.getOpenFileName()
    inputFile = filename[0]
    passNo = -1 
    return inputFile

def csv_reader(file):
    x, y, z, hole = array('d'), array('d'), array('d'), []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        try:
            line_count = 0
            for row in csv_reader:
                if (line_count == 0):
                    line_count = 1
                else:
                    x.append(float(row[0]))
                    y.append(float(row[1]))
                    z.append(float(row[2]))
                    hole.append(row[3])
        except:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
    return x, y, z, hole

def displayTable(self, fileName):
    global dateStr 
    global btype
    global bno
    global srno
    x, y, z,hole = csv_reader(fileName)
    self.tableWidget_pass2_coordinates.setRowCount(len(x))
    row =0
    for i in range(0,len(x)):
        self.tableWidget_pass2_coordinates.setItem(row, 0, QTableWidgetItem(str(i+1)))
        self.tableWidget_pass2_coordinates.setItem(row, 1, QTableWidgetItem(hole[i]))
        self.tableWidget_pass2_coordinates.setItem(row, 2, QTableWidgetItem(str(x[i])))
        self.tableWidget_pass2_coordinates.setItem(row, 3, QTableWidgetItem(str(y[i])))
        self.tableWidget_pass2_coordinates.setItem(row, 4, QTableWidgetItem(str(z[i])))
        row = row+1
        srno = row
    head_tail = os.path.split(fileName)
    file_path = re.split('[_ . \'d\']', head_tail[1])
    #['Proto', 'Boar', '55555', '75', 'Pass2', '20210714', 'csv']
    dateStr = file_path[5]
    self.lineEdit_date.setText(datetime.strptime(file_path[5], '%Y%m%d').strftime('%Y:%m:%d'))
    if file_path[0] == 'Prod':
        btype = 'Prod'
        self.lineEdit_btype.setText('Production')
    elif file_path[0] == 'Proto':
        btype = 'Proto'
        self.lineEdit_btype.setText('Prototype')
    bno = file_path[2]
    self.lineEdit_board_no.setText(bno)


# Action for Quit
def quit(self):
    QtWidgets.QApplication.quit()

# Checking if the directory exist
def check_dir(self):
    global dir_path
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print (dir_path)
    head_tail = os.path.split(dir_path)
    dir_path = head_tail[0]
    print (dir_path)
    if not os.path.exists(dir_path+"/data"): os.mkdir(dir_path+"/data")
    if not os.path.exists(dir_path+"/data/CSV"): os.mkdir(dir_path+"/data/CSV")
    if not os.path.exists(dir_path+ "/data/CSV/Pass3"): os.mkdir(dir_path+ "/data/CSV/Pass3")
    
    if not os.path.exists(dir_path+"/data/MC5"): os.mkdir(dir_path+"/data/MC5")
    if not os.path.exists(dir_path+ "/data/MC5/Pass3"): os.mkdir(dir_path+ "/data/MC5/Pass3")
    

# Tranfer action to remote server
def transfer(self):
    global pathPass3CSV
    global pathPass3MC5

    self.label_Finish_Pass.setText("TRANSFER START : ")
    self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password) # Protect password while typing
    
    # Get server Details
    SSHSERVER = self.lineEdit_server.text()
    SSHUSER = self.lineEdit_user.text()
    
    # If no value is enter set default value
    if (SSHSERVER == ''): 
        SSHSERVER = '158.144.55.17'
    if (SSHUSER == ''): 
        SSHUSER = 'sipm'

    # PASSWOD ROUTEEN TO BE UPDATED TO ACCEPT CORRECT VALUE
    self.lineEdit_password.setFocus()
    SSHPASS = self.lineEdit_password.text()
    error = 1
    if self.lineEdit_password.text() =="":
        print("Empty Value Not Allowed")
        self.lineEdit_password.setFocus()
    elif self.lineEdit_password.text() =="0":
        print("Enter non Zero Value")
        self.lineEdit_password.setFocus()
    else:
        SSHPASS = self.lineEdit_password.text()
        
    # Accept Destination Path
    DESTPATH = self.lineEdit_destinationPath.text()

    # DESTINATION PATH if not avalable create the folder NOT YET IMPLEMENTED 
    #check_dir(DESTPATH)    
    #mk_dir= "".join(["–rsync-path=" + '"' + "mkdir -p " + DESTPATH + " && rsync" +'”'])
    
    # Set Default path if no path is given
    if (DESTPATH == ''):
        DESTPATH = '~/automated_inspection/data/'

    # Display the values
    self.lineEdit_server.setText(SSHSERVER)
    self.lineEdit_user.setText(SSHUSER)
    self.lineEdit_destinationPath.setText(DESTPATH)

    print("Pass3 CSV  ",pathPass3CSV)
    print("Pass3 MC5  ",pathPass3MC5)
   

    # Transfer using rsync
#    cmdCSVPass0 = "".join(["sshpass -p "+ '"' + SSHPASS + '"' + " rsync -v " + pathPass0CSV + " " + SSHUSER + "@" + SSHSERVER + ":" + DESTPATH + "CSV/Pass0/. >>.transfer"])
    cmdCSVPass3 = "".join(["sshpass -p "+ '"' + SSHPASS + '"' + " rsync -v " + pathPass3CSV + " " + SSHUSER + "@" + SSHSERVER + ":" + DESTPATH + "CSV/Pass3/. >>.transfer"])
    cmdMC5Pass3 = "".join(["sshpass -p "+ '"' + SSHPASS + '"' + " rsync -v " + pathPass3MC5 + " " + SSHUSER + "@" + SSHSERVER + ":" + DESTPATH + "MC5/Pass3/. >>.transfer"])
    
    #errorCSVPass0 = os.system(cmdCSVPass0)
    errorCSVPass3 = os.system(cmdCSVPass3)
    errorMC5Pass3 = os.system(cmdMC5Pass3)
    #if errorCSVPass0 != 0:
    #    self.label_Finish_Pass.setStyleSheet("color: rgb(255, 28, 70);")  # Red
    #    self.label_Finish_Pass.setText("TRANSFER ERROR : CHECK THE REMORE SERVER DETAILS")
     #   self.lineEdit_server.setFocus()
    if errorCSVPass3 != 0:
        self.label_Finish_Pass.setStyleSheet("color: rgb(255, 28, 70);")  # Red
        self.label_Finish_Pass.setText("TRANSFER ERROR : CHECK THE REMORE SERVER DETAILS")
        self.lineEdit_server.setFocus()
    elif errorMC5Pass3 != 0:
        self.label_Finish_Pass.setStyleSheet("color: rgb(255, 28, 70);")  # Red
        self.label_Finish_Pass.setText("TRANSFER ERROR : CHECK THE REMORE SERVER DETAILS")
        self.lineEdit_server.setFocus()
    else:
        self.label_Finish_Pass.setStyleSheet("color: rgb(28, 43, 255);")  # Blue
        self.label_Finish_Pass.setText("TRANSFER COMPLETED : FILES TRANSFER TO REMORE SERVER COMPLETED")


# Reset all the values to accept new board details
def resetPass3(self):
    global flag
    flag = 0
    self.label_input_pass2_csv.setText("Input Pass2 CSV File")
    self.label_input_gerber_75.setText("Input 75 hole gerber file")

    self.lineEdit_date.setText("")
    self.lineEdit_time.setText("")
    self.lineEdit_btype.setText("")
    self.lineEdit_board_no.setText("")
    
    self.tableWidget_pass2_coordinates.setRowCount(0)
    
    self.label_output_CSV_pass3.setText("CSV pass3 File")
    self.label_output_MC5_pass3.setText("MC5 pass3 File")

    self.label_Finish_Pass.setText("")

    self.pushButton_Pass3.setEnabled(False)
    self.actionsave.setEnabled(False)
    self.pushButton_transfer.setEnabled(False)
    self.actiontransfer.setEnabled(False)

# Action to accept the values for mesured 7 holes and write to csv file
def pass3(self):
    global pathPass2CSV
    global pathPass3CSV
    global pathPass3MC5
    global inputGerber75
    global passNo
    global btype
    global bno
    global flag


    self.label_Finish_Pass.setStyleSheet("color: rgb(28, 43, 255);")  # Blue
    self.label_Finish_Pass.setText("PASS2 COORDINATES ACCEPTED")

# Action for generation the Offset and MC5 file

    # Find path to store the CSV file generated in pass3  
    pathPass3CSV = dir_path + '/data/CSV/Pass3/'
    pathPass3CSV= pathPass3CSV + btype + "_Board" + bno +"_Pass3_"+dateStr +".csv"

    # Generate string Proto_BoardXXXXX_Pass3.csv
    self.label_output_CSV_pass3.setText(pathPass3CSV)

    # Find path to store the MC5 file generated in pass3
    pathPass3MC5 = dir_path + '/data/MC5/Pass3/'
    pathPass3MC5= pathPass3MC5 + btype + "_Board" + bno +"_Pass3_"+dateStr +".mc5"

    # Generate string Proto_BoardXXXXX_Pass3.mc5
    self.label_output_MC5_pass3.setText(pathPass3MC5)
    
    # Call Mintus code for offset correction(CSV/Pass3/)
    #hole_offset_correction.offCorrection(gerber_corrected, pathPass2CSV, pathPass3CSV) 
    hole_offset_correction.offCorrection(inputGerber75, pathPass2CSV, pathPass3CSV) 
    
    # Call Mintus code for MC5 generation(MC5/Pass1)
    mc5file_genrater_final_with_XYZ.calculateMC5(pathPass3CSV, pathPass3MC5)
    
    self.label_Finish_Pass.setStyleSheet("color: rgb(28, 43, 255);")  # Blue
    self.label_Finish_Pass.setText("OFFSET FILE AND MC5 GENERATED")

    # Display default server values
    self.lineEdit_server.setPlaceholderText("158.144.55.17")
    self.lineEdit_user.setPlaceholderText("sipm")
    self.lineEdit_destinationPath.setPlaceholderText("~/automated_inspection/data/")

    self.pushButton_transfer.setEnabled(True)
    self.actiontransfer.setEnabled(True)

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
    ui = Ui_MainWindow_MiniGrantry_pass3()
    ui.setupUi(MainWindow)  
    
    MainWindow.showMaximized()
    #MainWindow.show()

    # time not uses
    ui.lineEdit_time.setHidden(True)
    ui.label_time.setHidden(True)
    
    # Fine Tuning for Table width and password
    ui.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
    header = ui.tableWidget_pass2_coordinates.horizontalHeader()
    #Interactive, Fixed, Stretch, ResizeToContents
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
    
    # call the action routeen
    ui.signals()

    # Exit the application on pressong the close (X) on the screen
    sys.exit(app.exec_())

# Start the application and initiate the GUI
if __name__ == "__main__":
    Ui_MainWindow_MiniGrantry_pass3.signals = signals
    Ui_MainWindow_MiniGrantry_pass3.quit = quit
    Ui_MainWindow_MiniGrantry_pass3.pass3 = pass3
    Ui_MainWindow_MiniGrantry_pass3.resetPass3 = resetPass3
    Ui_MainWindow_MiniGrantry_pass3.transfer = transfer
    Ui_MainWindow_MiniGrantry_pass3.file_handler=file_handler
    Ui_MainWindow_MiniGrantry_pass3.open_file_dialog_box=open_file_dialog_box
    Ui_MainWindow_MiniGrantry_pass3.diaplayTable=displayTable
    main()
