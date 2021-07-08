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
        cordinate_writer.writerow(["150.0", "0.0","0.0","0.0"])
        for i in range(0, len(x)):
            cordinate = [x[i], y[i], z[i],hole_off[i]]
            # print(cordinate)
            cordinate_writer.writerow(cordinate)


def propagate_offset(x_corc, y_corc, z_corc,import_csv_file,exported_csv_file):
    x, y, z,hole_off = csv_reader(import_csv_file)
    x_new, y_new, z_new = array('d'), array('d'), array('d')
    for i in range(0, len(x)):
        x_new.append(round(x[i] + x_corc,3))
        y_new.append(round(-y[i] + y_corc,3))
        z_new.append(round(z[i] - z_corc,3))
        #print(y_new, x_new, z_new)
    csv_writer(exported_csv_file, x_new, y_new, z_new,hole_off)


def offsect_cal(x_pcb,y_pcb,x_measured,y_measured):
    x_offset, y_offset = array('d'), array('d')
    for i in range(0,len(x_pcb)):
        x_offset.append(x_measured[i]-x_pcb[i])
        y_offset.append(y_measured[i]+y_pcb[i])
    return x_offset,y_offset


def propagate_offset_weighted(x_measured, y_measured,  z_measured, x_offset,y_offset,import_csv_file,exported_csv_file):
    x, y, z, hole = csv_reader(import_csv_file)
    x_cor, y_cor, z_cor = array('d'), array('d'), array('d')
    #print(hole)
    #
    print(x_cor)
    #loop over all hole of pcb
    for i in range(0,len(x)):
        #define array for the distance calculation
        norm = 0.0
        x_cor_temp = 0.0
        y_cor_temp = 0.0
        z_cor_temp = 0.0
        #loop over all measer point info given
        for disp in range(0,len(x_measured)):
            Di_invr = (pow(x_measured[disp] - (x_offset[disp] + x[i]), 2)+pow(y_measured[disp] - (y_offset[disp] - y[i]), 2))
            #when we look at the measured point only then displacement will be zero so for that assign weight = 1
            if(Di_invr<=1e-10): Di_invr=1
            else:Di_invr=1.0/Di_invr
            #print("z: ",z_measured[disp]," Di_inver = ",round(Di_invr,5))
            norm = norm + Di_invr
            x_cor_temp = x_cor_temp + ((x_offset[disp] + x[i]) * Di_invr)
            y_cor_temp = y_cor_temp + ((y_offset[disp] - y[i]) * Di_invr)
            z_cor_temp = z_cor_temp + (z_measured[disp] * Di_invr)
        x_cor.append(round((x_cor_temp / norm),3))
        y_cor.append(round((y_cor_temp / norm),3))
        z_cor.append(round((z_cor_temp / norm),3))
        csv_writer(exported_csv_file, x_cor, y_cor, z_cor, hole)
        #print("---------------------------------------------")
        
def offCorrection(fileName_75_pcb, parsed_csv , pathPass1CSV):
   
    global dir_path
    # read 7 hole values from gerber file
    fileName_7_pcb = dir_path + "/data/CSV/gerber/seven_hole_pcb.csv"
    x_pcb,y_pcb,z_pcb,hole_7 = csv_reader(fileName_7_pcb)

    # read 7 holes Measured Values
    #x_measured,y_measured,z_measured = csv_reader(fileName_7_measured)
    x_measured = []
    y_measured = []
    z_measured = []

    print(parsed_csv)
    sr_no_1, x_measured, y_measured, z_measured, hole_no_1 = map(list, zip(*parsed_csv))
    x_measured = [float(item) for item in x_measured]
    y_measured = [float(item) for item in y_measured]
    z_measured = [float(item) for item in z_measured]

    # Incase the values entered in table are zero
    if all([ v == 0 for v in x_measured ]):
        print ('measured values are zero')
        fileName_7_measured = dir_path + "/data/CSV/Pass0/hole_measure.csv"
        print("FILE NAME 7 MEASURED : " + fileName_7_measured)
        x_measured,y_measured,z_measured,hole_meas = csv_reader(fileName_7_measured)
    #print("slected holes = S01,S07,S73,S47,S43,S74,S69")
    date = datetime.datetime.now()
    #print("x_pcb = ", x_pcb)
    #print("y_pcb = ", y_pcb)
    print("x_measured = ",x_measured)
    print("y_measured = ", y_measured)
    print("z_measured = ", z_measured)
    ####define offset array#####
    x_offset, y_offset = array('d'), array('d')
    x_offset,y_offset = offsect_cal(x_pcb,y_pcb,x_measured,y_measured)
    #print("x_offset = ",x_offset)
    #print("y_offset = ", y_offset)

    #offsetCorrect = '../data/CSV/offset/check_offset_corrected_75.csv'
    propagate_offset_weighted(x_measured,y_measured,z_measured,x_offset,y_offset,fileName_75_pcb, pathPass1CSV)

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("USAGE: %s <seventy five pcb corrdinate csv file> <seven measured corrdinate csv file> <seven pcb corrdinate csv file>" % (sys.argv[0]))
        sys.exit(1)
    fileName_75_pcb = sys.argv[1]
    fileName_7_measured = sys.argv[2]
    fileName_7_pcb = sys.argv[3]

    offset_correction(fileName_75_pcb, fileName_7_measured, fileName_7_pcb) 
    
