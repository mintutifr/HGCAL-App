import ROOT as R
import numpy as np
from array import array
import csv
import sys
np.set_printoptions(threshold=sys.maxsize)

def csv_reader(file):
	x, y, = array('d'), array('d')
	with open(file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if (line_count == 0):
				line_count = 1
			#elif(float(row[0])<2 or float(row[1])<2):
				#pass
			else:
				x.append(float(row[1]))
				y.append(float(row[0]))
	return np.array(x), np.array(y)

def analyse_data_v07(filedir = "./", csvfile = "csv_Hexaboard_420", slopanderror = None):
	print("-----------------------------begin-----")
	print("file used : ",filedir,csvfile)
	imageNo = int(csvfile.rsplit("_",3)[2])
	print("image number = ",imageNo)
	holeNo = int(imageNo/5)+1
	print("ImageNo is : ",imageNo)
	print("HoleNo is : ",holeNo)

	# read csv file  
	x,y = csv_reader(csvfile+".csv")

	# remove evements which are less then 2
	x_index = np.argwhere(x < 2.0)
	print(np.take(x, x_index, axis=0))
	x = np.delete(x, x_index,axis=0)
	y = np.delete(y, x_index,axis=0)
	y_index = np.argwhere(y < 2.0)
	print(np.take(y, y_index, axis=0))
	x = np.delete(x, y_index,axis=0)
	y = np.delete(y, y_index,axis=0)
	print("index(x)  = %s  index(y) = %s"%(x_index,y_index))	
	print("len(x)  = %s  len(y) = %s"%(len(x),len(y)))
	#Find minimum and the maximum values of the x and the y
	xMax = np.amax(x)
	yMax = np.amax(y)
	xMin = np.amin(x)
	yMin = np.amin(y)
	print("xMax= %s xMin = %s yMax = %s yMin = %s"%(xMax,xMin,yMax,yMin))

	
	graph = R.TGraph(np.size(x),x,y)
	graph.Draw("Ap")	
	input()
if __name__ == "__main__":
	analyse_data_v07()
