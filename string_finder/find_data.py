import fileinput, string, sys, os, time, re

if len(sys.argv) != 2:
        print "USAGE: %s <input.txt> "%(sys.argv [0])
        sys.exit (1)

inputfile = sys.argv [1]

def search_string_in_file(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    list_of_results = []
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                #print line
		list_of_results.append(line)
    return list_of_results

ChangeToImageContext = search_string_in_file(inputfile,"Video.ChangeToImageContext")
print "size of array = ",len(ChangeToImageContext)
with open('ChangeToImageContext.csv','w') as f:
    f.write("X,Y,Z,Coax,Stage,Back,Frone,Right,Left,Angle,Color,NomMag\n")
    fi=0
    for line in ChangeToImageContext:
        #['1Video.ChangeToImageContext', '2', '3', '4X', '5', '40.006847483', '7', '8Y', '9', '138.176474440', '11', '12Z', '13', '31.780418770', '15', '16Coax', '17', '0.24', '19', '20Stage', '21', '0.00', '23', '24Back', '25', '0.00', '27', '28Front', '29', '0.21', '31', '32Right', '33', '0.00', '35', '36Left', '37', '0.00', '39', '40Angle', '41', '0.00', '43', '44Color', '45', '46', 'qvWhite', '48', 'NomMag', '50', '0.975000', '\n']
        if fi==0:
            line = re.split(",| |:|=|\r",line)
            f.write(line[5]+","+line[9]+","+line[13]+","+line[17]+","+line[21]+","+line[25]+","+line[29]+","+line[33]+","+line[37]+","+line[41]+","+line[46]+","+line[50]+"\n")
            fi+=1 
        else:
            #['1Video.ChangeToImageContext', '2', '3', '4X', '5', '183.072147483', '7', '8Y', '9', '119.523774440', '11', '12Z', '13', '31.772018770', '\n']i
            line = re.split(",| |:|=|\r",line)
            f.write(line[5]+","+line[9]+","+line[13]+"\n")
f.close()

FocusToolSetMode = search_string_in_file(inputfile,"FocusTool.SetMode")
print "size of array = ",len(FocusToolSetMode)
with open('FocusToolSetMode.csv','w') as f:
    #['1FocusTool.SetMode', '2', '3', '4FocusType', '5', 'SURFACE_ROTATE', '7', '8Speed', '9', 'MED', '11', '12Range', '13', '3.462603878', '\n']
    f.write("FocusType,Speed,Range\n")
    for line in FocusToolSetMode:
        line = re.split(",| |:|=|\r",line)
        f.write(line[5]+","+line[9]+","+line[13]+"\n")
f.close()

FocusToolRun = search_string_in_file(inputfile,"FocusTool.Run")
print "size of array = ",len(FocusToolRun)
with open('FocusToolRun.csv','w') as f:
    f.write("X,Y,Z,W,H,Angle\n")
    for line in FocusToolRun:
        line = re.split(",| |:|=|\r",line)
        f.write(line[5]+","+line[9]+","+line[13]+","+line[17]+","+line[21]+","+line[25]+"\n")
f.close()
