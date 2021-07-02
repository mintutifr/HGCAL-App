Canny Edge Detector Appliction and centroid finder algorithm 

Introduction:
This application can be used to plot the edges in a given image and also export them. Using the CSV file centroid of the stapped hole and be find with finder algorithm. 

Files:
'MyPyQT.py': This is the main application file
'requirements.txt':Contains names of all required packages


Dependencies:
Python v3.8+ 

1.1 ROOT has to compatible with the python version 
    
1.2 Install python 3.8 using: sudo apt-get install python3.8-venv

1.3 Install host certificate for the remote server required for the files transfer.

    # ssh user@server

example-

    # ssh sipm@158.144.55.17
    
    The authenticity of host '158.144.55.17 (158.144.55.17)' can't be established.
    ECDSA key fingerprint is SHA256:i9AHPM/u9ZfIqsUOda58UYKV6lgIH38pDRj9/RDohx6dA.
    Are you sure you want to continue connecting (yes/no)? yes
    
1.4 Install "sshpass" utility this is used to provid user password for rsync command

    For Ubuntu systems:  # sudo apt install sshpass
    
    For Linux systems :  # yum install sshpass
    
    For MAC systems   :  # brew install hudochenkov/sshpass/sshpass
    
   
1.5 Directory structure as given bellow should be available on remote server

example- directory: sub_directory_1   sub_directory_2 ....
    
      data           : Canny_Images  Centroid_Images  CSV  MC5  Raw_Images
      
    ./Canny_Images   : Pass1  Pass2  Pass3
    
    ./Centroid_Images: Pass1  Pass2  Pass3
    
    ./CSV            : gerber  Pass0  Pass1  Pass2  Pass3
    
    ./MC5            : Pass1  Pass2  Pass3
    
    ./Raw_Images     :  

1.5 Clone the repository https://github.com/mintutifr/HGCAL-App.git

How to run:

2. Activate your Python Virtual environment

   Steps to generate a vitrual environment

      1. Open terminal

      2. Select or create a folder where you want to create the environment (let say you want to create one inside the cloned repository)

      3. Enter "cd HGCAL-App"

      4. Enter "python3.8 -m venv pcb-ENV"

      5. Enter "source pcb-ENV/bin/activate"

      6. Your terminal will be directed to use the activated environment. (Eg (pcb-ENV) $username:)

      7. To deactivate the inviroment again type "deactivate"

3. Browse to the directory with files

4. Type 

   pip install -r requirements.txt

   This will install all the necessary packages required to run the app

5. Run the app by typing 

   python3.8  MyPyQT.py

6. if you get core dump with the following error massage:

   "qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
    This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem."

    use the following command:

     1. export QT_DEBUG_PLUGINS=1

     2. sudo apt-get install libxcb-xinerama0

7. In the app choose the images focused folder

8. The image preview is displayed.

9. To view the corresponding edges detected, click 'Process' button.

10. The result is displayed on the bottom.

11. You may go through the set of images in the folder by clicking 'Next' or 'Previous'.

12. You can also export the corresponding .csv file containing the coordinates of the edges for each image. csv file will be stored in same directory where image exist and have the same name as the image with csv extension 
