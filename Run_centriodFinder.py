import fileinput, string, sys, os, time, subprocess

if len(sys.argv) != 2:
                print("USAGE: %s <input dir>"%(sys.argv[0]))
                sys.exit(1)

Dir = sys.argv[1]
if not os.path.dirname(Dir+"centroid"): 
    os.mkdir(Dir+"centroid")
os.mkdir(Dir+"centroid")    
csvfiles = os.listdir(Dir)
print(csvfiles)
for fille in csvfiles:
    csv_file_wo_ext=fille.split(".")[0]
    cmd_createWorkspace = "root -l -b -q "+"'analyse_data.C("+'"'+Dir+'","'+csv_file_wo_ext+'")'+"'"
    print(cmd_createWorkspace)
    os.system(cmd_createWorkspace)

