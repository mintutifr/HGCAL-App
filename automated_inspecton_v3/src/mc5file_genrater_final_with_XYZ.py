import fileinput, string, sys, os, time, datetime
import csv




def csv_reader(line_no):
    csv_file = open(fileName,"r")
    csv_reader = csv.reader(csv_file, delimiter=',')
    for n in range(-1,line_no):    
        line_text_csv = next(csv_reader)
    return line_text_csv

def PTP_MOTION_CMD(step):
    return '      <command step="'+str(step)+'" cmd_id="00" cmd_name="PTP MOTION" status="0">\n'
def parameter_abs_inc():
    return '        <parameter abs_inc="0"/>\n'
def end_CMD():
    return '      </command>\n'
def TIMER_CMD(step):
    return '      <command step="'+str(step)+'" cmd_id="06" cmd_name="TIMER" status="0">\n'
def parameter_time():
    return '        <parameter time=" +5.00"/>\n'
def parameter_out_ch101():
    return '        <parameter out_ch="101"/>\n'
def parameter_out_ch103():
    return '        <parameter out_ch="103"/>\n'
def CALL_CH_CMD(step):
    return '      <command step="'+str(step)+'" cmd_id="07" cmd_name="CALL CH." status="0">\n'

def calculateMC5(pathPass1CSV, pathPass1MC5):
    f = open(pathPass1MC5,"w")
    line_count_csv = 0
    linecounter=1;
    
    for line in fileinput.input("Header.mc5"):
        f.write(line)

    with open(pathPass1CSV) as csv_file:
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
                new_line_sintex = '        <point name="EndPoint" X=" +'+row[0]+'" Y=" +'+row[1]+'" Z="  +'+row[2]+'"/>\n'
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
                new_line_sintex = '        <point name="EndPoint" X=" +'+row[0]+'" Y=" +'+row[1]+'"/>\n'
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

if __name__ == "__main__":
    
#    if len(sys.argv) != 3:
 #       print "USAGE: %s <input csv file name > <output mc5 file name >"%(sys.argv [0])
#        sys.exit (1)
    pathPass1CSV  = sys.argv[1]
    pathPass1MC5  = sys.argv[2]
    date   = datetime.datetime.now()
    calculateMC5(pathPass1CSV, pathPass1MC5)
