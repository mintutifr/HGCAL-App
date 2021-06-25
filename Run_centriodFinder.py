import fileinput, string, sys, os, time, subprocess
import ROOT as R
from array import *    
import numpy as np
R.gInterpreter.ProcessLine('#include "analyse_data_v07.C"')
if len(sys.argv) != 2:
                print("USAGE: %s <input dir>"%(sys.argv[0]))
                sys.exit(1)

Dir = sys.argv[1]
print(os.path.isdir(Dir+"../Centroid/"))
if not os.path.isdir(Dir+"../Centroid/"): 
    os.mkdir(Dir+"../Centroid")
#os.mkdir(Dir+"../Centroid")    
csvfiles = os.listdir(Dir)
slopanderror = np.zeros(13)
print(csvfiles)

for fille in csvfiles:
    csv_file_wo_ext=fille.split(".")[0]
    print(''+Dir+','+csv_file_wo_ext+'')
    try:
        R.analyse_data_v07(Dir,csv_file_wo_ext,slopanderror)
    except Exception as e:
        print(e)
        print("code crash")


    #cmd_createWorkspace = "root -l -b -q "+"'analyse_data_v07.C("+'"'+Dir+'","'+csv_file_wo_ext+'")'+"'"
    #print(cmd_createWorkspace)
    #os.system(cmd_createWorkspace)
