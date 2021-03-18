Canny Edge Detector Appliction

Introduction:
This application can be used to plot the edges in a given image and also export them.

Files:
'pcb.py': This is the main application file
'requirements.txt':Contains names of all required packages


Dependencies:
Python v3.8+
1. Install python 3.8 using: sudo apt-get install python3.8-venv

How to run:
2. Activate your Python Virtual environment
   Steps to generate a vitrual environment
      1. Open terminal
      2. Select or create a folder where you want to create the environment
      3. Enter "cd folderName"
      4. Enter "python3.8 -m venv pcb-ENV"
      5. Enter "source pcb-ENV/bin/activate"
      6. Your terminal will be directed to use the activated environment. (Eg (pcb-ENV) $username:)
      7. TO deactivate the inviroment again type "deactivate"
3. Browse to the directory with files
4. Type 
   pip install -r requirements.txt
   This will install all the necessary packages required to run the app
5. Run the app by typing 
   python3.8 pcb.py
6. if you get core dump with the following error massage:
   "qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
    This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem."
    use the following command:
     $ export QT_DEBUG_PLUGINS=1
     $ sudo apt-get install libxcb-xinerama0
7. In the app choose the images focused folder
8. The image preview is displayed.
9. To view the corresponding edges detected, click 'Process' button.
10. The result is displayed on the bottom.
11. You may go through the set of images in the folder by clicking 'Next' or 'Previous'.
12. You can also export the corresponding .csv file containing the coordinates of the edges for each image.
