Canny Edge Detector Appliction and centroid finder algorithm 

This pakage has two graphical user interface which can be used separately

Introduction GUI1:  MC5 files can be created using the /automated_inspecton/src/automated_inspection.py and then created MC5 tranfered to any server with given credential.
    
Introduction GU2:  This application can be used to plot the edges in a given image and also export them. Using the CSV file centroid of the stapped hole can be find with centroid finder algorithm. 

Files:

    'automated_inspection.py':  This is the main application file file for GUI
    'MyPyQT.py': This is the second main application file
    'requirements.txt':Contains names of all required packages


Dependencies: 

1.1 Python v3.8+ and ROOT has to be compatible with the used python version 
    
1.2 Install python 3.8 using: 

    sudo apt-get install python3.8-venv
    
1.3 root can be installed from the cern offical website:

    https://root.cern/install/
    
1.4 Install host certificate for the remote server required for the files transfer (only if data need to tranfered to another server).

    # ssh user@server

example-

    # ssh sipm@158.144.55.17
    
    The authenticity of host '158.144.55.17 (158.144.55.17)' can't be established.
    ECDSA key fingerprint is SHA256:i9AHPM/u9ZfIqsUOda58UYKV6lgIH38pDRj9/RDohx6dA.
    Are you sure you want to continue connecting (yes/no)? yes
    
1.5 Install "sshpass" utility this is used to provid user password for rsync command (only if data need to tranfered to another server)

    For Ubuntu systems:  # sudo apt install sshpass
    
    For Linux systems :  # yum install sshpass
    
    For MAC systems   :  # brew install hudochenkov/sshpass/sshpass
    
   
1.5 Directory structure as given bellow should be available on remote server (only if data need to tranfered to another server)

example- directory: sub_directory_1   sub_directory_2 ....
    
      data           : Canny_Images  Centroid_Images  CSV  MC5  Raw_Images
      
    ./Canny_Images   : Pass1  Pass2  Pass3
    
    ./Centroid_Images: Pass1  Pass2  Pass3
    
    ./CSV            : gerber  Pass0  Pass1  Pass2  Pass3
    
    ./MC5            : Pass1  Pass2  Pass3
    
    ./Raw_Images     :  

1.5 Clone the repository https://github.com/mintutifr/HGCAL-App.git

How to run:

2. Setup a vitrual environment with Python and Activate

      1. Open terminal

      2. Select or create a folder where you want to create the environment (let say you want to create one inside the cloned repository)

      3. Enter 

        cd HGCAL-App

      4. Enter 

        python3.8 -m venv pcb-ENV

      5. Enter 

        source pcb-ENV/bin/activate

      6. Your terminal will be directed to use the activated environment. (Eg (pcb-ENV) $username:)

      7. To deactivate the inviroment again type "deactivate"

4.  After activation of the invironment one can install the required pakages with the following command

        pip install -r requirements.txt

5. Run the app by typing 

        python3.8  MyPyQT.py

6. if you get core dump while runing MyPyQT.py after suceesful installment of all pakages with the following error massage :

   "qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
    This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem."

    then use the following command to get rid of this error:

        export QT_DEBUG_PLUGINS=1
        sudo apt-get install libxcb-xinerama0

    once this this done try to run the MyPyQT.py again

7. In the app click on the "import image" button and choose the images focused folder. This will display the image preview all required path are stored in the script automatically.

9. To view the corresponding edges detected, click on 'Process' button. The result is displayed in the GUI.

11. one may go through the set of images in the folder by clicking 'Next' or 'Previous'.

12. one can also export the corresponding .csv file containing the coordinates of the edges for each image by clicking on "export csv" button. csv file will be stored in a sub directory name "CSV" where image exist and have the same name as the image with csv extension. And with that this button also run the centroid finder algoritham (uses root) using these exported csv fils . It is espected the code will cash if python version is not comatible root.
