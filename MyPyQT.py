from PyQt5.QtWidgets import QMainWindow, QFileDialog, QFrame, QApplication, QPushButton, QDialog, QGroupBox, \
	QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QWidget
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
import os, cv2, sys
import numpy as np
import pandas as pd

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

		Exit_Button = QPushButton(" Exit App    ", self)
		Exit_Button.setGeometry(QtCore.QRect(10, 310, 135, 45))
		Exit_Button.setMaximumSize(QtCore.QSize(16777215, 16777215))
		Exit_Button.setIcon(QtGui.QIcon("exit.jpeg"))
		Exit_Button.setIconSize(QtCore.QSize(43, 43))
		Exit_Button.setToolTip("<h2> click here to Exit the application<h2>")
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		Exit_Button.setFont(font)
		Exit_Button.clicked.connect(self.CloseMe)

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

		grilayout = QGridLayout()
		grilayout.addWidget(self.labelImgname, 1, 0)
		grilayout.addWidget(self.labelImg, 2, 0)  # , 1, 2)#(self.labelImg, 0, 1)
		grilayout.addWidget(self.labelcan, 3, 0)

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
			if not os.path.exists(dirpath+"/CSV"): os.mkdir(dirpath+"/CSV")
			if not os.path.exists(dirpath+"/canny"): os.mkdir(dirpath + "/canny")
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
			(thresh, blackAndWhiteImage) = cv2.threshold(img_erosion, 250, 255, cv2.THRESH_BINARY)
			self.tight = cv2.Canny(blackAndWhiteImage, 240, 255)
			self.coordinates = np.argwhere(self.tight == 255)
			self.y, self.x = zip(*self.coordinates)
			self.Draw_Image(self.tight)

			cv2.imwrite(os.path.dirname(self.fileList[self.currentImg])+"/canny/canny_"+self.fileList[self.currentImg].split(".")[0].split("/")[-1] + ".jpeg",self.tight)
			print(os.path.dirname(self.fileList[self.currentImg])+"/canny/canny_"+self.fileList[self.currentImg].split(".")[0].split("/")[-1] + ".jpeg")
			print( "saving file " + self.fileList[self.currentImg].split(".")[0]+".jpeg")

		except:
			print("Please select the image first")
			pass

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
			print( "csv file ",(self.fileList[self.currentImg].split("."))[0]+".csv" ,"exported")
			#pd.DataFrame(self.coordinates).to_csv((self.fileList[self.currentImg].split("."))[0]+".csv", index=False,header=['y_coord', 'x_coord'])
			pd.DataFrame(self.coordinates).to_csv(os.path.dirname(self.fileList[self.currentImg])+"/CSV/csv_"+self.fileList[self.currentImg].split(".")[0].split("/")[-1] + ".csv", index=False,header=['y_coord', 'x_coord'])
		except:
			print("Please select the image first")
			pass

	def Canny_detector(img, weak_th=None, strong_th=None):

		# conversion of image to grayscale
		img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		# Noise reduction step
		img = cv2.GaussianBlur(img, (5, 5), 1.4)


		# Calculating the gradients
		gx = cv2.Sobel(np.float32(img), cv2.CV_64F, 1, 0, 3)
		gy = cv2.Sobel(np.float32(img), cv2.CV_64F, 0, 1, 3)

		# Conversion of Cartesian coordinates to polar
		mag, ang = cv2.cartToPolar(gx, gy, angleInDegrees=True)

		# setting the minimum and maximum thresholds
		# for double thresholding
		mag_max = np.max(mag)
		if not weak_th: weak_th = mag_max * 0.1
		if not strong_th: strong_th = mag_max * 0.5

		# getting the dimensions of the input image
		height, width = img.shape

		# Looping through every pixel of the grayscale
		# image
		for i_x in range(width):
			for i_y in range(height):

				grad_ang = ang[i_y, i_x]
				grad_ang = abs(grad_ang - 180) if abs(grad_ang) > 180 else abs(grad_ang)

				# selecting the neighbours of the target pixel
				# according to the gradient direction
				# In the x axis direction
				if grad_ang <= 22.5:
					neighb_1_x, neighb_1_y = i_x - 1, i_y
					neighb_2_x, neighb_2_y = i_x + 1, i_y

				# top right (diagnol-1) direction
				elif grad_ang > 22.5 and grad_ang <= (22.5 + 45):
					neighb_1_x, neighb_1_y = i_x - 1, i_y - 1
					neighb_2_x, neighb_2_y = i_x + 1, i_y + 1

				# In y-axis direction
				elif grad_ang > (22.5 + 45) and grad_ang <= (22.5 + 90):
					neighb_1_x, neighb_1_y = i_x, i_y - 1
					neighb_2_x, neighb_2_y = i_x, i_y + 1

				# top left (diagnol-2) direction
				elif grad_ang > (22.5 + 90) and grad_ang <= (22.5 + 135):
					neighb_1_x, neighb_1_y = i_x - 1, i_y + 1
					neighb_2_x, neighb_2_y = i_x + 1, i_y - 1

				# Now it restarts the cycle
				elif grad_ang > (22.5 + 135) and grad_ang <= (22.5 + 180):
					neighb_1_x, neighb_1_y = i_x - 1, i_y
					neighb_2_x, neighb_2_y = i_x + 1, i_y

				# Non-maximum suppression step
				if width > neighb_1_x >= 0 and height > neighb_1_y >= 0:
					if mag[i_y, i_x] < mag[neighb_1_y, neighb_1_x]:
						mag[i_y, i_x] = 0
						continue

				if width > neighb_2_x >= 0 and height > neighb_2_y >= 0:
					if mag[i_y, i_x] < mag[neighb_2_y, neighb_2_x]:
						mag[i_y, i_x] = 0

			weak_ids = np.zeros_like(img)
			strong_ids = np.zeros_like(img)
			ids = np.zeros_like(img)

			# double thresholding step
			for i_x in range(width):
				for i_y in range(height):

					grad_mag = mag[i_y, i_x]

					if grad_mag < weak_th:
						mag[i_y, i_x] = 0
					elif strong_th > grad_mag >= weak_th:
						ids[i_y, i_x] = 1
					else:
						ids[i_y, i_x] = 2

			# finally returning the magnitude of
			# gradients of edges
			return mag

class Example_Window(QDialog):
	def __init__(self):
		super().__init__()

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

		self.createlayout()
		vbox = QVBoxLayout()
		vbox.addWidget(self.groupbox)

		label = QLabel("This is PyQT5 GUI Application Development")
		label.setFont(QtGui.QFont("Sanserif", 15))
		label.setStyleSheet('color:blue')

		vbox.addWidget(label)
		self.setLayout(vbox)

	def createlayout(self):
		button_folder = QPushButton("import Img", self)
		button_folder.setGeometry(QRect(100, 100, 60, 28))  # (x,y,deltaX,deltaY)
		button_folder.setIcon(QtGui.QIcon("image_icon.jpeg"))
		button_folder.setIconSize(QtCore.QSize(40, 40))
		# button_folder.setMinimumHeight(40)
		button_folder.setToolTip("<h2> click here to import the image from the selected folder<h2>")
		button_folder.clicked.connect(self.loadImage)

		button_Img = QPushButton("select the folder", self)
		button_Img.setGeometry(QRect(100, 100, 60, 28))  # (x,y,deltaX,deltaY)
		button_Img.setIcon(QtGui.QIcon("folder_icon.jpeg"))
		button_Img.setIconSize(QtCore.QSize(40, 40))
		# button_Img.setMinimumHeight(40)
		button_Img.setToolTip("<h2> click here to select the folder<h2>")
		button_Img.clicked.connect(self.CloseMe)

		button_Img_next = QPushButton("Next Img", self)
		button_Img_next.setGeometry(QRect(100, 100, 60, 28))  # (x,y,deltaX,deltaY)
		button_Img_next.setIcon(QtGui.QIcon("next_Img.jpeg"))
		button_Img_next.setIconSize(QtCore.QSize(40, 40))
		button_Img_next.setMinimumHeight(40)
		button_Img_next.setToolTip("<h2> click here to select the next Image<h2>")
		button_Img_next.clicked.connect(self.nextImage)

		self.labelImg = QLabel("This is PyQT5 GUI Application Development")
		# layout.addWidget(self.label, 0, 0, 1, 2)
		self.labelImg.setMinimumSize(200, 200)
		self.labelImg.setAlignment(QtCore.Qt.AlignCenter)

		self.labelcan = QLabel("This is PyQT5 GUI Application Development")
		# layout.addWidget(self.label, 0, 0, 1, 2)
		self.labelcan.setMinimumSize(200, 200)
		self.labelcan.setAlignment(QtCore.Qt.AlignCenter)

		grilayout = QGridLayout()
		grilayout.addWidget(button_Img, 0, 0)
		grilayout.addWidget(button_folder, 0, 1)
		grilayout.addWidget(button_Img_next, 0, 2)
		grilayout.addWidget(self.labelImg, 1, 0)  # , 1, 2)#(self.labelImg, 0, 1)
		grilayout.addWidget(self.labelcan, 1, 1)

		self.groupbox = QGroupBox(" try this for arrange the buttens")
		self.groupbox.setLayout(grilayout)

	def CloseMe(self):
		sys.exit()

	def nextImage(self):
		# ensure that the file list has not been cleared due to missing files
		if self.fileList:
			try:
				filename = next(self.dirIterator)
				print(filename)
				pixmap = QtGui.QPixmap(filename).scaled(self.labelcan.size(),
														QtCore.Qt.KeepAspectRatio)
				if pixmap.isNull():
					# the file is not a valid image, remove it from the list
					# and try to load the next one
					self.fileList.remove(filename)
					self.nextImage()
				else:
					self.labelcan.setPixmap(pixmap)
			except:
				# the iterator has finished, restart it
				self.dirIterator = iter(self.fileList)
				self.nextImage()
		else:
			# no file list found, load an image
			self.loadImage()

	def loadImage(self):
		filename, _ = QtWidgets.QFileDialog.getOpenFileName(
			self, 'Select Image', '', 'Image Files (*.png *.jpg *.jpeg)')
		if filename:
			pixmap = QtGui.QPixmap(filename).scaled(self.labelImg.size(),
													QtCore.Qt.KeepAspectRatio)
			if pixmap.isNull():
				return
			self.labelImg.setPixmap(pixmap)
			dirpath = os.path.dirname(filename)

			self.fileList = []
			for f in os.listdir(dirpath):
				fpath = os.path.join(dirpath, f)
				if os.path.isfile(fpath) and f.endswith(('.png', '.jpg', '.jpeg')):
					self.fileList.append(fpath)
			self.fileList.sort()
			self.dirIterator = iter(self.fileList)
			# print(filename)
			# print(next(self.dirIterator))
			while True:
				# cycle through the iterator until the current file is found
				if next(self.dirIterator) == filename:
					break


class Example_Window2_hori(QDialog):
	def __init__(self):
		super().__init__()

		self.title = "TIFR HGCAL Development"
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

		self.createlayout()
		vbox = QVBoxLayout()
		vbox.addWidget(self.groupbox)
		self.setLayout(vbox)

	def createlayout(self):
		self.groupbox = QGroupBox("GUI")
		hboxlayout = QHBoxLayout()

		button1 = QPushButton("select the folder", self)
		button1.setGeometry(QRect(30, 80, 131, 61))  # (x,y,deltaX,deltaY)
		button1.setIcon(QtGui.QIcon("folder_icon.jpeg"))
		# button1.setIconSize(QtCore.QSize(40,40))
		button1.setMaximumSize(QtCore.QSize(16777215, 16777215))
		# button.setMinimumHeight(40)
		button1.setToolTip("<h2> click here to select the folder<h2>")
		button1.clicked.connect(self.CloseMe)

		button = QPushButton("import Img", self)
		button.setGeometry(QRect(180, 110, 331, 271))  # (x,y,deltaX,deltaY)
		button.setIcon(QtGui.QIcon("image_icon.jpeg"))
		# button.setIconSize(QtCore.QSize(40, 40))
		# button.setMinimumHeight(40)
		button.setToolTip("<h2> click here to import the image from the selected folder<h2>")

		hboxlayout.addWidget(button1)
		hboxlayout.addWidget(button)
		self.groupbox.setLayout(hboxlayout)

	def CloseMe(self):
		sys.exit()


class Example_Window3_vert(QDialog):
	def __init__(self):
		super().__init__()

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

		self.createlayout()
		vbox = QVBoxLayout()
		vbox.addWidget(self.groupbox)

		label = QLabel("This is PyQT5 GUI Application Development")
		label.setFont(QtGui.QFont("Sanserif", 15))
		label.setStyleSheet('color:blue')

		vbox.addWidget(label)
		self.setLayout(vbox)

	def createlayout(self):
		button_folder = QPushButton("import Img", self)
		button_folder.setGeometry(QRect(100, 100, 60, 28))  # (x,y,deltaX,deltaY)
		button_folder.setIcon(QtGui.QIcon("image_icon.jpeg"))
		button_folder.setIconSize(QtCore.QSize(40, 40))
		# button_folder.setMinimumHeight(40)
		button_folder.setToolTip("<h2> click here to import the image from the selected folder<h2>")
		button_folder.clicked.connect(self.loadImage)

		button_Img = QPushButton("select the folder", self)
		button_Img.setGeometry(QRect(100, 100, 60, 28))  # (x,y,deltaX,deltaY)
		button_Img.setIcon(QtGui.QIcon("folder_icon.jpeg"))
		button_Img.setIconSize(QtCore.QSize(40, 40))
		# button_Img.setMinimumHeight(40)
		button_Img.setToolTip("<h2> click here to select the folder<h2>")
		button_Img.clicked.connect(self.CloseMe)

		button_Img_next = QPushButton("Next Img", self)
		button_Img_next.setGeometry(QRect(100, 100, 60, 28))  # (x,y,deltaX,deltaY)
		button_Img_next.setIcon(QtGui.QIcon("next_Img.jpeg"))
		button_Img_next.setIconSize(QtCore.QSize(40, 40))
		button_Img_next.setMinimumHeight(40)
		button_Img_next.setToolTip("<h2> click here to select the next Image<h2>")
		button_Img_next.clicked.connect(self.nextImage)

		self.labelImg = QLabel("This is PyQT5 GUI Application Development")
		# layout.addWidget(self.label, 0, 0, 1, 2)
		self.labelImg.setMinimumSize(200, 200)
		self.labelImg.setAlignment(QtCore.Qt.AlignCenter)

		self.labelcan = QLabel("This is PyQT5 GUI Application Development")
		# layout.addWidget(self.label, 0, 0, 1, 2)
		self.labelcan.setMinimumSize(200, 200)
		self.labelcan.setAlignment(QtCore.Qt.AlignCenter)

		grilayout = QGridLayout()
		grilayout.addWidget(button_Img, 0, 0)
		grilayout.addWidget(button_folder, 0, 1)
		grilayout.addWidget(button_Img_next, 0, 2)
		grilayout.addWidget(self.labelImg, 1, 0)  # , 1, 2)#(self.labelImg, 0, 1)
		grilayout.addWidget(self.labelcan, 1, 1)

		self.groupbox = QGroupBox(" try this for arrange the buttens")
		self.groupbox.setLayout(grilayout)

	def CloseMe(self):
		sys.exit()

	def nextImage(self):
		# ensure that the file list has not been cleared due to missing files
		if self.fileList:
			try:
				filename = next(self.dirIterator)
				print(filename)
				pixmap = QtGui.QPixmap(filename).scaled(self.labelcan.size(),
														QtCore.Qt.KeepAspectRatio)
				if pixmap.isNull():
					# the file is not a valid image, remove it from the list
					# and try to load the next one
					self.fileList.remove(filename)
					self.nextImage()
				else:
					self.labelcan.setPixmap(pixmap)
			except:
				# the iterator has finished, restart it
				self.dirIterator = iter(self.fileList)
				self.nextImage()
		else:
			# no file list found, load an image
			self.loadImage()

	def loadImage(self):
		filename, _ = QtWidgets.QFileDialog.getOpenFileName(
			self, 'Select Image', '', 'Image Files (*.png *.jpg *.jpeg)')
		if filename:
			pixmap = QtGui.QPixmap(filename).scaled(self.labelImg.size(),
													QtCore.Qt.KeepAspectRatio)
			if pixmap.isNull():
				return
			self.labelImg.setPixmap(pixmap)
			dirpath = os.path.dirname(filename)

			self.fileList = []
			for f in os.listdir(dirpath):
				fpath = os.path.join(dirpath, f)
				if os.path.isfile(fpath) and f.endswith(('.png', '.jpg', '.jpeg')):
					self.fileList.append(fpath)
			self.fileList.sort()
			self.dirIterator = iter(self.fileList)
			# print(filename)
			# print(next(self.dirIterator))
			while True:
				# cycle through the iterator until the current file is found
				if next(self.dirIterator) == filename:
					break


class Example_ImageLoader(QtWidgets.QWidget):
	def __init__(self):
		QtWidgets.QWidget.__init__(self)
		layout = QtWidgets.QGridLayout(self)
		self.label = QtWidgets.QLabel()
		layout.addWidget(self.label, 0, 0, 1, 2)
		self.label.setMinimumSize(200, 200)
		self.label.setAlignment(QtCore.Qt.AlignCenter)

		self.loadImagebutton = QtWidgets.QPushButton("Import image")
		layout.addWidget(self.loadImagebutton, 1, 0)

		self.nextImagebutton = QtWidgets.QPushButton("Next Image")
		layout.addWidget(self.nextImagebutton)

		self.loadImagebutton.clicked.connect(self.loadImage)
		self.nextImagebutton.clicked.connect(self.nextImage)

		self.dirItertor = None
		self.fileList = []
		self.show()

	def loadImage(self):
		filename, _ = QtWidgets.QFileDialog.getOpenFileName(
			self, 'Select Image', '', 'Image Files (*.png *.jpg *.jpeg)')
		if filename:
			pixmap = QtGui.QPixmap(filename).scaled(self.label.size(),
													QtCore.Qt.KeepAspectRatio)
			if pixmap.isNull():
				return
			self.label.setPixmap(pixmap)
			dirpath = os.path.dirname(filename)

			self.fileList = []
			for f in os.listdir(dirpath):
				fpath = os.path.join(dirpath, f)
				if os.path.isfile(fpath) and f.endswith(('.png', '.jpg', '.jpeg')):
					self.fileList.append(fpath)
			self.fileList.sort()
			self.dirIterator = iter(self.fileList)
			# print(filename)
			# print(next(self.dirIterator))
			while True:
				# cycle through the iterator until the current file is found
				if next(self.dirIterator) == filename:
					break

	def nextImage(self):
		# ensure that the file list has not been cleared due to missing files
		if self.fileList:
			try:
				filename = next(self.dirIterator)
				pixmap = QtGui.QPixmap(filename).scaled(self.label.size(),
														QtCore.Qt.KeepAspectRatio)
				if pixmap.isNull():
					# the file is not a valid image, remove it from the list
					# and try to load the next one
					self.fileList.remove(filename)
					self.nextImage()
				else:
					self.label.setPixmap(pixmap)
			except:
				# the iterator has finished, restart it
				self.dirIterator = iter(self.fileList)
				self.nextImage()
		else:
			# no file list found, load an image
			self.loadImage()


class Example_Window_frame(QWidget):
	def __init__(self):
		super().__init__()

		self.title = "frame"
		self.top = 100
		self.left = 100
		self.width = 400
		self.height = 300

		self.InitWindow()
		self.setLayout(self.hbox)
		self.Creatbutton()
		self.show()

	def InitWindow(self):
		path = QApplication.applicationDirPath()
		self.setWindowIcon(QtGui.QIcon('main_icon.jpeg'))
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)
		self.setStyleSheet("background-color:yellow")

		frame1 = QFrame()
		frame1.setFrameShape(QFrame.StyledPanel)
		frame1.setStyleSheet("background-color:red")
		frame1.setLineWidth(6)

		frame2 = QFrame()
		frame2.setFrameShape(QFrame.StyledPanel)
		frame2.setStyleSheet("background-color:green")
		frame2.setLineWidth(6)

		button = QPushButton("import Img", frame2)
		# button.move(50,50)
		button.setGeometry(QRect(50, 50, 120, 28))  # (x,y,deltaX,deltaY)
		button.setIcon(QtGui.QIcon("tifr-logo-blue.png"))
		button.setIconSize(QtCore.QSize(40, 40))
		button.setToolTip("<h2> click here to import the image<h2>")
		# button.clicked.connect(self.Print)
		button.clicked.connect(self.CloseMe)

		self.hbox = QHBoxLayout()
		self.hbox.addWidget(frame1)

		# self.hbox.addWidget(self.Creatbutton())

	def Creatbutton(self):
		button = QPushButton("import Img", self)
		# button.move(50,50)
		button.setGeometry(QRect(50, 50, 120, 28))  # (x,y,deltaX,deltaY)
		button.setIcon(QtGui.QIcon("tifr-logo-blue.png"))
		button.setIconSize(QtCore.QSize(40, 40))
		button.setToolTip("<h2> click here to import the image<h2>")
		# button.clicked.connect(self.Print)
		button.clicked.connect(self.CloseMe)

	def createlayout(self):
		self.groupbox = QGroupBox("GUI")
		hboxlayout = QHBoxLayout()

	def Print(slef):
		print("Hello world")

	def CloseMe(self):
		sys.exit()


if __name__ == "__main__":
	App = QApplication(sys.argv)
	window = My_main_Window()
	sys.exit(App.exec())
