import fileinput, string, sys, os, time, datetime
import csv

if len(sys.argv) != 2:
        print "USAGE: %s <input csv file name >"%(sys.argv [0])
        sys.exit (1)

fileName  = sys.argv[1]
date   = datetime.datetime.now()


def csv_reader(line_no):
    csv_file = open(fileName,"r")
    csv_reader = csv.reader(csv_file, delimiter=',')
    for n in range(-1,line_no):    
        line_text_csv = next(csv_reader)
    return line_text_csv

def PTP_MOTION_CMD(step):
    return '      <command step="'+str(step)+'" cmd_id="00" cmd_name="PTP MOTION" status="0">\r\n'
def parameter_abs_inc():
    return '        <parameter abs_inc="0"/>\r\n'
def end_CMD():
    return '      </command>\r\n'
def TIMER_CMD(step):
    return '      <command step="'+str(step)+'" cmd_id="06" cmd_name="TIMER" status="0">\r\n'
def parameter_time():
    return '        <parameter time=" +5.00"/>\r\n'
def parameter_out_ch101():
    return '        <parameter out_ch="101"/>\r\n'
def parameter_out_ch103():
    return '        <parameter out_ch="103"/>\r\n' 
def CALL_CH_CMD(step):
    return '      <command step="'+str(step)+'" cmd_id="07" cmd_name="CALL CH." status="0">\r\n'
f = open("mc5_example_xyz_cor.mc5","w")
line_count_csv = 0
linecounter=1;

for line in fileinput.input("Header.mc5"):
    f.write(line)

with open(fileName) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    step = 0
    for row in csv_reader:
        if(line_count_csv==0):
	   line_count_csv+=1
	   step = line_count_csv
	   continue
	elif(len(row)==3):
	     	f.write(PTP_MOTION_CMD(step))
	    	f.write(parameter_abs_inc())
	    	new_line_sintex = '        <point name="EndPoint" X=" +'+row[0]+'" Y=" +'+row[1]+'" Z="  +'+row[2]+'"/>\r\n'
	    	f.write(new_line_sintex)
	    	f.write(end_CMD())
		step+=1

		if(step==2):
		    f.write(TIMER_CMD(step))
                    f.write(parameter_time())
		else: 
		    f.write(CALL_CH_CMD(step))
		    f.write(parameter_out_ch103())
		    f.write(end_CMD())
		    step+=1
		    f.write(CALL_CH_CMD(step))
		    f.write(parameter_out_ch101())
                f.write(end_CMD())
		step+=1
	elif(len(row)==2):
		f.write(PTP_MOTION_CMD(step))
		f.write(parameter_abs_inc())
		new_line_sintex = '        <point name="EndPoint" X=" +'+row[0]+'" Y=" +'+row[1]+'"/>\r\n'
		f.write(new_line_sintex)
		f.write(end_CMD())
		step+=1
		
		f.write(CALL_CH_CMD(step))
		f.write(parameter_out_ch101())
		f.write(end_CMD())
		step+=1
	line_count_csv+=1

for line in fileinput.input("Bottom.mc5"):
    f.write(line)

f.close()

