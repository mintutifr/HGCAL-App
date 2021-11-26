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
slopanderror = np.zeros(24)
print(csvfiles)

Rootfile = R.TFile("slopsAndOffset_pass2.root", 'recreate')
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
x_offset = array('d',[0])
y_offset = array('d',[0])

hole = array('d',[0])

int_xL1 = array('d',[0])
int_xL2 = array('d',[0])
int_xL3 = array('d',[0])
int_yL1 = array('d',[0])
int_yL2 = array('d',[0])
int_yL3 = array('d',[0])

tree.Branch("slop_L1A",  slop_L1A,  'slop_L1A/D')#0
tree.Branch("slopError_L1A", slopError_L1A, 'slopError_L1A/D')#1
tree.Branch("slop_L1B",  slop_L1B,  'slop_L1B/D')#2
tree.Branch("slopError_L1B", slopError_L1B, 'slopError_L1B/D')#3

tree.Branch("slop_L2A",  slop_L2A,  'slop_L2A/D')#4
tree.Branch("slopError_L2A", slopError_L2A, 'slopError_L2A/D')#5
tree.Branch("slop_L2B",  slop_L2B,  'slop_L2B/D')#6
tree.Branch("slopError_L2B", slopError_L2B, 'slopError_L2B/D')#7

tree.Branch("slop_L3A",  slop_L3A,  'slop_L3A/D')#8
tree.Branch("slopError_L3A", slopError_L3A, 'slopError_L3A/D')#9
tree.Branch("slop_L3B",  slop_L3B,  'slop_L3B/D')#10
tree.Branch("slopError_L3B", slopError_L3B, 'slopError_L3B/D')#11

tree.Branch("offset", offset, 'offset/D')#12
tree.Branch("image", image, 'image/D')#13

tree.Branch("x_offset", x_offset, 'x_offset/D')#14
tree.Branch("y_offset", y_offset, 'y_offset/D')#15

tree.Branch("hole", hole, 'hole/D')#16

tree.Branch("int_xL1", int_xL1, 'int_xL1/D')#17
tree.Branch("int_xL2", int_xL2, 'int_xL2/D')#18
tree.Branch("int_xL3", int_xL3, 'int_xL3/D')#19

tree.Branch("int_yL1", int_yL1, 'int_yL1/D')#20
tree.Branch("int_yL2", int_yL2, 'int_yL2/D')#21
tree.Branch("int_yL3", int_yL3, 'int_yL3/D')#22

for fille in csvfiles:
    csv_file_wo_ext=fille.split(".")[0]
    print(''+Dir+','+csv_file_wo_ext+'')

    try:
        R.analyse_data_v07(Dir,csv_file_wo_ext,slopanderror,"1")
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
        x_offset[0] = slopanderror[14]
        y_offset[0] = slopanderror[15]

        print("x_offset : ",x_offset[0], "y_offset : ",y_offset[0])
        hole[0] = slopanderror[16]

        int_xL1[0] = slopanderror[17]
        int_xL2[0] = slopanderror[18]
        int_xL3[0] = slopanderror[19]

        int_yL1[0] = slopanderror[20]
        int_yL2[0] = slopanderror[21]
        int_yL3[0] = slopanderror[22]
        tree.Fill()
        #exit()
    except Exception as e:
        print(e)
        print("code crash")

Rootfile.Write()
Rootfile.Close()
    #cmd_createWorkspace = "root -l -b -q "+"'analyse_data_v07.C("+'"'+Dir+'","'+csv_file_wo_ext+'")'+"'"
    #print(cmd_createWorkspace)
    #os.system(cmd_createWorkspace)
