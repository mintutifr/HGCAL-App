#  x,y,z,board_no-board_type-date-time :  7 hole file structure

#import standard programs
import sys, os, glob, csv, re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
from subprocess import call, PIPE, Popen
#from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
#from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem, QMessageBox
#from PyQt5.QtWidgets import QLineEdit
import pathlib
#import user programs
from automated_inspection_gui import *
import hole_offset_correction 
import mc5file_genrater_final_with_XYZ

# Declar Global variables
global dateStr 
global pathPass0CSV
global pathPass1CSV
global passNo
global btype
global bno
global inputGerber75
global item
global dir_path

dir_path = os.path.dirname(os.path.realpath(__file__))
head_tail = os.path.split(dir_path)
dir_path = head_tail[0]
print (dir_path)

# Check the actions to be performed (Button of Menu)
def signals(self):
    resetPass0(self) # Reset before we begain
    self.lineEdit_board_no.editingFinished.connect(self.validate_board)# Accept only valid board number

    # quit action by button or by menu (QUIT)
    self.pushButton_quit.clicked.connect(self.quit)
    self.actionquit.triggered.connect(self.quit)
    
    # Reset action by button or by menu (RESET)
    self.pushButton_reset_pass0.clicked.connect(self.resetPass0)
    self.actionreset.triggered.connect(self.resetPass0)

    # Perform action to generate the Offset file and MC5 file (SAVE)
    self.pushButton_Pass0.clicked.connect(self.pass0)
    self.actionsave.triggered.connect(self.pass0)

    # Commented as to remove Pass0 Pass1 different action
    #self.pushButton_Pass1.clicked.connect(self.pass1)

    # Perform transfer action by button or by menu (TRANSFER)
    self.pushButton_transfer.clicked.connect(self.transfer)
    self.actiontransfer.triggered.connect(self.transfer)

    # Call action Canny_Edge_Detector
    #self.actionCanny_Edge_Detector.triggered.connect(self.CannyEdgeDetector)

# For acception numeric table values
class NumericDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super(NumericDelegate, self).createEditor(parent, option, index)
        if isinstance(editor, QLineEdit):
            reg_ex = QRegExp("-?\d{0,}(?:\.\d{0,})?")
            validator = QRegExpValidator(reg_ex, editor)
            editor.setValidator(validator)
        return editor

# Action for Quit
def quit(self):
    QtWidgets.QApplication.quit()

# Action for Button and menu status (enable/disable)
def getButtonStatus(self):
    global passNo 
    if passNo == -1: # Save action buttons enabled (disable transfer button)
        self.pushButton_Pass0.setEnabled(True)
        self.actionsave.setEnabled(True)
        self.pushButton_Pass1.setEnabled(False)
        self.pushButton_Pass1.setHidden(True)
        self.pushButton_transfer.setEnabled(False)
        self.actiontransfer.setEnabled(False)
        self.pushButton_transfer.setHidden(True)
       
        self.lineEdit_server.setHidden(True)
        self.lineEdit_user.setHidden(True)
        self.lineEdit_password.setHidden(True)
        self.lineEdit_destinationPath.setHidden(True)
        self.label_server_details.setHidden(True)
    elif passNo == 0: # Save action Pass1 : feature disabled
        self.pushButton_Pass0.setEnabled(False)
        self.actionsave.setEnabled(False)
        self.pushButton_Pass0.setHidden(True)
        self.pushButton_Pass1.setEnabled(True)
        self.actionsave.setEnabled(True)
        self.pushButton_Pass1.setHidden(False)

        self.lineEdit_server.setHidden(True)
        self.lineEdit_user.setHidden(True)
        self.lineEdit_password.setHidden(True)
        self.lineEdit_destinationPath.setHidden(True)
        self.label_server_details.setHidden(True)
    elif passNo == 1: # Transfer action buttons enabled (disable save button)
        self.pushButton_Pass0.setEnabled(False)
        self.actionsave.setEnabled(False)
        self.pushButton_Pass0.setHidden(False)
        self.pushButton_Pass1.setEnabled(False)
        self.pushButton_Pass1.setHidden(True)
        self.pushButton_transfer.setEnabled(True)
        self.actiontransfer.setEnabled(True)
        self.pushButton_transfer.setHidden(False)

        self.lineEdit_server.setHidden(False)
        self.lineEdit_user.setHidden(False)
        self.lineEdit_password.setHidden(False)
        self.lineEdit_destinationPath.setHidden(False)
        self.label_server_details.setHidden(False)
    else: # Reset action enabled (diasble save and transfer buttons)
        self.pushButton_Pass0.setEnabled(False)
        self.actionsave.setEnabled(False)
        self.pushButton_Pass0.setHidden(False)
        self.pushButton_Pass1.setEnabled(False)
        self.pushButton_Pass1.setHidden(True)
        self.pushButton_transfer.setEnabled(False)
        self.actiontransfer.setEnabled(False)
        self.pushButton_transfer.setHidden(True)

        self.lineEdit_server.setHidden(True)
        self.lineEdit_user.setHidden(True)
        self.lineEdit_password.setHidden(True)
        self.lineEdit_destinationPath.setHidden(True)
        self.label_server_details.setHidden(True)


# Checking if the directory exist this will be used when reomte transfer to new directory
def check_dir(od_dir):
    if not os.path.exists(od_dir):
        print(os_dir, " dose not exist.")
        exit(1)

# Tranfer action to remote server
def transfer(self):

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
    
    # Transfer using rsync
    cmdCSVPass0 = "".join(["sshpass -p "+ '"' + SSHPASS + '"' + " rsync -v " + pathPass0CSV + " " + SSHUSER + "@" + SSHSERVER + ":" + DESTPATH + "CSV/Pass0/. >>.transfer"])
    cmdCSVPass1 = "".join(["sshpass -p "+ '"' + SSHPASS + '"' + " rsync -v " + pathPass1CSV + " " + SSHUSER + "@" + SSHSERVER + ":" + DESTPATH + "CSV/Pass1/. >>.transfer"])
    cmdMC5Pass1 = "".join(["sshpass -p "+ '"' + SSHPASS + '"' + " rsync -v " + pathPass1MC5 + " " + SSHUSER + "@" + SSHSERVER + ":" + DESTPATH + "MC5/Pass1/. >>.transfer"])
    
    errorCSVPass0 = os.system(cmdCSVPass0)
    errorCSVPass1 = os.system(cmdCSVPass1)
    errorMC5Pass1 = os.system(cmdMC5Pass1)
    #print ("CSV Pass0 Error :: ", errorCSVPass0," CSV Pass1 Error: ", errorCSVPass1," MC5 Pass1 Error ::" ,errorMC5Pass1)
    if errorCSVPass0 != 0:
        self.label_Finish_Pass.setStyleSheet("color: rgb(255, 28, 70);")  # Red
        self.label_Finish_Pass.setText("TRANSFER ERROR : CHECK THE REMORE SERVER DETAILS")
        self.lineEdit_server.setFocus()
    elif errorCSVPass1 != 0:
        self.label_Finish_Pass.setStyleSheet("color: rgb(255, 28, 70);")  # Red
        self.label_Finish_Pass.setText("TRANSFER ERROR : CHECK THE REMORE SERVER DETAILS")
        self.lineEdit_server.setFocus()
    elif errorMC5Pass1 != 0:
        self.label_Finish_Pass.setStyleSheet("color: rgb(255, 28, 70);")  # Red
        self.label_Finish_Pass.setText("TRANSFER ERROR : CHECK THE REMORE SERVER DETAILS")
        self.lineEdit_server.setFocus()
    else:
        self.pushButton_quit.setEnabled(True)
        self.pushButton_reset_pass0.setEnabled(True)
        self.label_Finish_Pass.setStyleSheet("color: rgb(28, 43, 255);")  # Blue
        self.label_Finish_Pass.setText("TRANSFER COMPLETED : FILES TRANSFER TO REMORE SERVER COMPLETED")

# Accept the vaild board value
def validate_board(self):
    global pathPass0CSV
    global passNo
    global btype
    global bno
    global dir_path

    if self.lineEdit_board_no.text() =="":
        print("Empty Value Not Allowed")
        self.lineEdit_board_no.setFocus()
    elif self.lineEdit_board_no.text() =="0":
        print("Enter non Zero Value")
        self.lineEdit_board_no.setFocus()
    else:
        bno = self.lineEdit_board_no.text()
        
        # Find path to store the CSV file generated in pass0  
        pathPass0CSV = dir_path + '/data/CSV/Pass0/'
    
        if "Production" == (self.comboBox_board_type.currentText()):
            btype = "Prod"
            self.label_output_CSV_pass0.setText('Prod_BoardXXXXX_Pass0_07.csv')
            self.label_output_CSV_pass1.setText('Prod_BoardXXXXX_75_Pass1.csv')
            self.label_output_MC5_pass1.setText('Prod_BoardXXXXX_75_Pass1.mc5')
        else:
            btype = "Proto" 
            self.label_output_CSV_pass0.setText('Proto_BoardXXXXX_Pass0_07.csv')
            self.label_output_CSV_pass1.setText('Proto_BoardXXXXX_75_Pass1.csv')
            self.label_output_MC5_pass1.setText('Proto_BoardXXXXX_75_Pass1.mc5')


        bno = bno.rjust(5, '0')
        self.lineEdit_board_no.setText(bno)
        #self.lineEdit_board_no.setReadOnly(True)
        # Generate file name Proto_BoardXXXXX_Pass0_07.csv
        pathPass0CSV= pathPass0CSV + btype + "_Board" + bno +"_Pass0_07_"+dateStr +".csv"
        self.label_output_CSV_pass0.setText(pathPass0CSV)
        
        passNo = -1
        getButtonStatus(self)
        
        self.tableWidget_7_coordinates.setFocus()
        self.tableWidget_7_coordinates.setCurrentCell(0, 2)
    
        return

# Reset all the values to accept new board details
def resetPass0(self):
    setDateTime(self)
    self.lineEdit_board_no.setReadOnly(False)
    self.label_Finish_Pass.setStyleSheet("color: rgb(5, 0, 1);")  # Black
    self.label_Finish_Pass.setText("")


    self.lineEdit_board_no.setText('')
    self.lineEdit_board_no.setCursorPosition(0)
    self.label_output_CSV_pass0.setText('')
    self.label_output_CSV_pass1.setText('')
    self.label_output_MC5_pass1.setText('')
    nrows = self.tableWidget_7_coordinates.rowCount()
    ncols = self.tableWidget_7_coordinates.columnCount()

    for row in range(0,nrows):
        for col in range(2, ncols):
            self.tableWidget_7_coordinates.setItem(row,col, QTableWidgetItem("0"))
    #self.comboBox_board_type.setFocus(True)
    self.lineEdit_board_no.setFocus()
    self.label_output_CSV_pass0.setText('ProXX_BoardXXXXX_Pass0_07.csv')
    self.label_output_CSV_pass1.setText('ProXX_BoardXXXXX_75_Pass1.csv')
    self.label_output_MC5_pass1.setText('ProXX_BoardXXXXX_75_Pass1.mc5')

    global passNo
    passNo = 2
    getButtonStatus(self)

# Action to accept the values for mesured 7 holes and write to csv file
def pass0(self):
    global pathPath0CSV
    global passNo
    global btype
    global bno
    global item

    validate_board(self)

    with open(pathPass0CSV, 'w', newline='') as pass0_file:
        writer = csv.DictWriter(pass0_file, fieldnames = [('Board Type:',btype), ('Board No:',bno), ('Date:', dateStr)])
        writer = csv.DictWriter(pass0_file, fieldnames = ["Sr. no", "X", "Y", "Z", "Hole no."])
                
        writer.writeheader()
        writer = csv.writer(pass0_file)
        item = []
        nrows = self.tableWidget_7_coordinates.rowCount()
        ncols = self.tableWidget_7_coordinates.columnCount()
        for row in range(0,nrows):
            item_text = []
            cell = self.tableWidget_7_coordinates.item(row, 0)
            item_text.append(cell.text())
            #for col in range(0, ncols):
            for col in range(2, ncols):
                cell = self.tableWidget_7_coordinates.item(row, col)
                item_text.append(cell.text())
            cell = self.tableWidget_7_coordinates.item(row, 1)
            item_text.append(cell.text())
            item.append(item_text)
            writer.writerow(item[row])
        
        # Get Ready for Pass1
        self.label_input_gerber_75_pass1.setText(getGerber75())

        self.label_Finish_Pass.setStyleSheet("color: rgb(28, 43, 255);")  # Blue
        self.label_Finish_Pass.setText("PASS0 COMPLETED : MANUAL COORDINATES ACCEPTED")
        passNo = 0
        getButtonStatus(self)

        # Call action for generation Offset file and MC5 file
        pass1(self)

# Action to get the gerber file : curently hard coded
def getGerber75():

    global dir_path
    # open inputGerber75 and get inputGerber7
    global inputGerber75
    inputGerber75 = dir_path + "/data/CSV/gerber/pcb_cordinate_75.csv"
    return inputGerber75

# Action for generation the Offset and MC5 file
def pass1(self):
    global pathPass1CSV
    global pathPass1MC5
    global inputGerber75
    global inputGerber7
    global pathPath0CSV
    global item
    global dir_path

    # Find path to store the CSV file generated in pass1  
    pathPass1CSV = dir_path + '/data/CSV/Pass1/'
    pathPass1CSV= pathPass1CSV + btype + "_Board" + bno +"_75_Pass1_"+dateStr +".csv"

    # Generate string Proto_BoardXXXXX_75_Pass1.csv
    self.label_output_CSV_pass1.setText(pathPass1CSV)

    # Find path to store the MC5 file generated in pass1  
    pathPass1MC5 = dir_path + '/data/MC5/Pass1/'
    pathPass1MC5= pathPass1MC5 + btype + "_Board" + bno +"_75_Pass1_"+dateStr +".mc5"

    # Generate string Proto_BoardXXXXX_75_Pass1.mc5
    self.label_output_MC5_pass1.setText(pathPass1MC5)
    
    # Call Mintus code for offset correction(CSV/Pass1/)
    hole_offset_correction.offCorrection(inputGerber75, item, pathPass1CSV) 
    
    # Call Mintus code for MC5 generation(MC5/Pass1)
    mc5file_genrater_final_with_XYZ.calculateMC5(pathPass1CSV, pathPass1MC5)
    
    self.label_Finish_Pass.setStyleSheet("color: rgb(28, 43, 255);")  # Blue
    self.label_Finish_Pass.setText("OFFSET FILE AND MC5 GENERATED")

    global passNo
    passNo = 1
    getButtonStatus(self)
    
    # Display default server values
    self.lineEdit_server.setPlaceholderText("158.144.55.17")
    self.lineEdit_user.setPlaceholderText("sipm")
    self.lineEdit_destinationPath.setPlaceholderText("~/automated_inspection/data/")
    self.lineEdit_server.setFocus()

    # Enter Default values in the mesured table if values entered are zero
    sr_no_1, x_measured, y_measured, z_measured, hole_no_1 = map(list, zip(*item))
    x_measured = [float(item) for item in x_measured]
    y_measured = [float(item) for item in y_measured]
    z_measured = [float(item) for item in z_measured]
    if all([ v == 0 for v in x_measured ]): # Incase the values entered in table are zero
        print ('Measured values are zero: Displaying default measured values')
        mhole_path = dir_path + "/data/CSV/Pass0/hole_measure.csv"
        with open(mhole_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            row =0
            for frow in reader:
                self.tableWidget_7_coordinates.setItem(row, 2, QTableWidgetItem(frow[0]))
                self.tableWidget_7_coordinates.setItem(row, 3, QTableWidgetItem(frow[1]))
                self.tableWidget_7_coordinates.setItem(row, 4, QTableWidgetItem(frow[2]))
                row = row +1
    self.lineEdit_password.setFocus()

# Set the Date and time for the values to be entered
def setDateTime(self):
    global dateStr
    date = datetime.today().strftime('%Y:%m:%d')
    dateStr = date.replace(":", "")
    self.lineEdit_date.setText(date)
    self.lineEdit_date.setReadOnly(True)

    time = datetime.today().strftime('%H:%M:%S')
    self.lineEdit_time.setText(time)
    self.lineEdit_time.setReadOnly(True)

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
    ui = Ui_MainWindow_MiniGrantry()
    ui.setupUi(MainWindow)  
    
    MainWindow.showMaximized()
    #MainWindow.show()

    # Fine Tuning for Table width and password
    ui.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
    header = ui.tableWidget_7_coordinates.horizontalHeader()
    #Interactive, Fixed, Stretch, ResizeToContents
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
    #Accept numeric values in tabel
    delegate = NumericDelegate(ui.tableWidget_7_coordinates)
    ui.tableWidget_7_coordinates.setItemDelegate(delegate)
    
    # call the action routeen
    ui.signals()

    # Exit the application on pressong the close (X) on the screen
    sys.exit(app.exec_())

# Start the application and initiate the GUI
if __name__ == "__main__":
    Ui_MainWindow_MiniGrantry.signals = signals
    Ui_MainWindow_MiniGrantry.quit = quit
    Ui_MainWindow_MiniGrantry.pass0 = pass0
    Ui_MainWindow_MiniGrantry.pass1 = pass1
    Ui_MainWindow_MiniGrantry.resetPass0 = resetPass0
    Ui_MainWindow_MiniGrantry.transfer = transfer
    Ui_MainWindow_MiniGrantry.validate_board=validate_board
    main()
