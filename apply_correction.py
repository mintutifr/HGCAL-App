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
        #cordinate_writer.writerow(["150.0", "0.0","0.0","0.0"])
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



def apply_offset_correction(fileName_offset_from_centroid_finder,fileName_offset_not_appalied_input_file,fileName_offset_applied_output_file):
   
    #global dir_path
    # read csv file which contains offset

    x_offset,y_offset,z_offset,hole_offset = csv_reader(fileName_offset_from_centroid_finder)

    # read csv file which contains x,y coordinate
    x,y,z,hole = csv_reader(fileName_offset_not_appalied_input_file)

    x_new, y_new, z_new,hole_new = array('d'), array('d'),array('d'),[]

    #print(len(hole),len(hole_offset))
    for ii in range(0,len(hole)):
        for jj in range(0, len(hole_offset)):
            #print(ii, ",", jj)
            if(hole[ii]==hole_offset[jj]):
                x_new.append(round(x[ii]+x_offset[jj],3))
                y_new.append(round(y[ii] + y_offset[jj],3))
                z_new.append(round(x[ii] + z_offset[jj],3))
                hole_new.append(hole[ii])
                #print(x[ii], ",", x_offset[jj], ",", x[ii]+x_offset[jj], y[ii], ",", y_offset[jj], ",", y[ii]+y_offset[jj],
                print(hole[ii],",", hole_offset[jj])
                break
    csv_writer(fileName_offset_applied_output_file, x_new, y_new, z_new, hole_new)
    #print(hole_new)
    #for jj in range(0, len(hole_offset)):
        #print(hole_offset[jj],",",hole_new[jj])

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("USAGE: %s <csv file contain offset from the centriod> <csv file on which offset will be applaied> <csv file for output>" % (sys.argv[0]))
        sys.exit(1)
    fileName_offset_from_centroid_finder = sys.argv[1]
    fileName_offset_not_appalied_input_file = sys.argv[2]
    fileName_offset_applied_output_file = sys.argv[3]
    #print(dir_path)

    apply_offset_correction(fileName_offset_from_centroid_finder,fileName_offset_not_appalied_input_file,fileName_offset_applied_output_file)
    
