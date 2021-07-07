import fileinput, string, sys, os, time, subprocess
import ROOT as R
from array import *    
import numpy as np
R.gInterpreter.ProcessLine('#include "analyse_data_v07.C"')
if len(sys.argv) != 2:
                print("USAGE: %s <input dir>"%(sys.argv[0]))
                sys.exit(1)

Dir = sys.argv[1]
if not os.path.dirname(Dir+"centroid"): 
    os.mkdir(Dir+"centroid")
#os.mkdir(Dir+"centroid")    
csvfiles = os.listdir(Dir)
slopanderror = np.zeros(14)
print(csvfiles)

Rootfile = R.TFile("slopsAndOffset.root", 'recreate')
tree = R.TTree("tree_name", "tree title")

slop_L1A = array('d',[0])
slopError_L1A = array('d',[0])
slop_L1B = array('d',[0])
slopError_L1B = array('d',[0])

slop_L2A = array('d',[0])
slopError_L2A = array('d',[0])
slop_L2B = array('d',[0])
slopError_L2B = array('d',[0])

slop_L3A = array('d',[0])
slopError_L3A = array('d',[0])
slop_L3B = array('d',[0])
slopError_L3B = array('d',[0])

offset = array('d',[0])
image = array('d',[0])

tree.Branch("slop_L1A",  slop_L1A,  'slop_L1A/D')
tree.Branch("slopError_L1A", slopError_L1A, 'slopError_L1A/D')
tree.Branch("slop_L1B",  slop_L1B,  'slop_L1B/D')
tree.Branch("slopError_L1B", slopError_L1B, 'slopError_L1B/D')

tree.Branch("slop_L2A",  slop_L2A,  'slop_L2A/D')
tree.Branch("slopError_L2A", slopError_L2A, 'slopError_L2A/D')
tree.Branch("slop_L2B",  slop_L2B,  'slop_L2B/D')
tree.Branch("slopError_L2B", slopError_L2B, 'slopError_L2B/D')

tree.Branch("slop_L3A",  slop_L3A,  'slop_L3A/D')
tree.Branch("slopError_L3A", slopError_L3A, 'slopError_L3A/D')
tree.Branch("slop_L3B",  slop_L3B,  'slop_L3B/D')
tree.Branch("slopError_L3B", slopError_L3B, 'slopError_L3B/D')

tree.Branch("offset", offset, 'offset/D')
tree.Branch("image", image, 'image/D')
for fille in csvfiles:
    csv_file_wo_ext=fille.split(".")[0]
    print(''+Dir+','+csv_file_wo_ext+'')
    try:
        R.analyse_data_v07(Dir,csv_file_wo_ext,slopanderror)
        print(slopanderror)
        slop_L1A[0]  = slopanderror[0]
        slopError_L1A[0]= slopanderror[1]
        slop_L1B[0]  = slopanderror[2]
        slopError_L1B[0]= slopanderror[3]

        slop_L2A[0]  = slopanderror[4]
        slopError_L2A[0]= slopanderror[5]
        slop_L2B[0]  = slopanderror[6]
        slopError_L2B[0]= slopanderror[7]

        slop_L3A[0]  = slopanderror[8]
        slopError_L3A[0]= slopanderror[9]
        slop_L3B[0]  = slopanderror[10]
        slopError_L3B[0]= slopanderror[11]

        offset[0]=slopanderror[12]
        image[0] = slopanderror[13]
        tree.Fill()
    except Exception as e:
        print(e)
        print("code crash")

Rootfile.Write()
Rootfile.Close()

    #cmd_createWorkspace = "root -l -b -q "+"'analyse_data_v07.C("+'"'+Dir+'","'+csv_file_wo_ext+'")'+"'"
    #print(cmd_createWorkspace)
    #os.system(cmd_createWorkspace)
