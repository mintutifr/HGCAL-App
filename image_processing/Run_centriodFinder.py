import fileinput, string, sys, os, time, subprocess
import ROOT as R
from array import *    
import numpy as np
import csv
R.gInterpreter.ProcessLine('#include "analyse_data_v07.C"')
#if len(sys.argv) != 2:
        #        print("USAGE: %s <input dir>"%(sys.argv[0]))
         #       sys.exit(1)

#Dir = os.getcwd() #sys.argv[1]
#print(os.path.isdir(Dir+"/../data/Centroid/Pass1"))
#if not os.path.isdir(Dir+"/../data/Centroid/Pass1"):
    #os.mkdir(Dir+"/../data/Centroid/Pass1")
#os.mkdir(Dir+"../Centroid")
def Run_centriodFinder_inloop(inDir_forcsvfiles,outDir_towriteCSVfile):
    Dir=inDir_forcsvfiles
    csvfiles = os.listdir(Dir)
    slopanderror = np.zeros(24)
    print(csvfiles)
    title = ['x_offset','y_offset','z_offset','hole','image']
    entries = []
    for file in csvfiles:
        print(file,file.find("Pass"))
        if(file.find("Pass")!=-1): continue
        csv_file_wo_ext=file.split(".")[0]
        print(''+Dir+','+csv_file_wo_ext+'')
        try:
            R.analyse_data_v07(Dir,csv_file_wo_ext,slopanderror)
            #print(slopanderror[14])
            event= [round(slopanderror[14],3),round(slopanderror[15],3),0.0,'S'+str(int(slopanderror[16])).zfill(2),int(slopanderror[13])]
            entries.append(event)
            pass
        except Exception as e:
            print(e)
            print("code crash")

    # name of csv file
    # writing to csv file
    with open(outDir_towriteCSVfile, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        # writing the title
        csvwriter.writerow(title)
        # writing the data rows
        csvwriter.writerows(entries)

        #cmd_createWorkspace = "root -l -b -q "+"'analyse_data_v07.C("+'"'+Dir+'","'+csv_file_wo_ext+'")'+"'"
        #print(cmd_createWorkspace)
        #os.system(cmd_createWorkspace)
    print("file ",outDir_towriteCSVfile, " has been created")