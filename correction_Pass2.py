import fileinput, string, sys, os, time, datetime
import csv
from array import array
import math

global dir_path
dir_path = os.path.dirname(os.path.realpath(__file__))
head_tail = os.path.split(dir_path)
dir_path = head_tail[0]


def csv_reader(file):
    x, y, z, hole = array('d'), array('d'), array('d'), []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if (line_count == 0):
                line_count = 1
            else:
                x.append(float(row[0]))
                y.append(float(row[1]))
                z.append(float(row[2]))
                hole.append(row[3])
    return x, y, z, hole


def csv_writer(file, x, y, z,hole_off):
    with open(file, mode='w') as cordinate_file:
        cordinate_writer = csv.writer(cordinate_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        cordinate_writer.writerow(["X", "Y","Z","hole"])
#        cordinate_writer.writerow(["150.0", "0.0","0.0","0.0"])
        for i in range(0, len(x)):
            cordinate = [x[i], y[i], z[i],hole_off[i]]
            # print(cordinate)
            cordinate_writer.writerow(cordinate)


def CorrectionPass2(fileName_offset, fileName_75_gerber , pathPass2CSV):
   
    global dir_path
    x_pcb,y_pcb,z_pcb,hole = csv_reader(fileName_75_gerber)
    x_off,y_off,z_off,hole_off = csv_reader(fileName_offset)

    x_cor = []
    y_cor = []
    z_cor = []
    hole_cor = []
    
    for i in range(len(hole_off)): 
        if hole_off[i] in hole :
            index = hole.index(hole_off[i])
            x_cor.append(x_pcb[index])
            y_cor.append(y_pcb[index])
            z_cor.append(z_pcb[index])
            hole_cor.append(hole[index])
    
    csv_writer(pathPass2CSV, x_cor, y_cor, z_cor, hole_cor)


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("USAGE: %s <offset from centroid Finder csv file> <Gerber pcb 75 corrdinate csv file> <Corrected file for pass2 corrdinate csv file>" % (sys.argv[0]))
        sys.exit(1)

    fileName_offset = sys.argv[1]
    fileName_75_gerber = sys.argv[2]
    fileName_Corrected_Pass2 = sys.argv[3]

    CorrectionPass2(fileName_offset, fileName_75_gerber,fileName_Corrected_Pass2) 
    
