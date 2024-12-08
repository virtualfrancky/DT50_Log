from datetime import datetime
import time
import re
from pathlib import Path

ROOT_DIR = Path.cwd()
F_Log = input('Please type the Log file with .txt at the end : \n')
TEXT_FILE = ROOT_DIR / F_Log
#TEXT_FILE = ROOT_DIR / 'DT50_Log.txt'


def driver_version(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        driver_line = lines[0]
        if re.search(r'G2', driver_line):
            print('Driver G2 used')
        else:
            print('Driver G1 used')

def serial_master(file_path, sn_M):
    with open(file_path, 'r') as file: #open the file
        lines = file.readlines() # read all lines
        for line in lines: #for each line in variable lines
            if line.find(sn_M) != -1: # if sn is found
                serial_master = line[25:33] # store serial number in variable serial_master
                print('Serial Number of Master is:', serial_master) # print the serial number
    return serial_master

def serial_client_1(file_path, sn_C_1):
    with open(file_path, 'r') as file: #open the file
        lines = file.readlines() # read all lines
        for line in lines: #for each line in variable lines
            if line.find(sn_C_1) != -1: # if sn is found
                serial_client_1 = line[25:33] # store serial number in variable serial_client_1
                print('Serial Number of Client N°1 is:', serial_client_1) # print the serial number of client 1
    return serial_client_1

        

def Batch_Run(file_path):
    with open(file_path, 'r') as file: #open the file
        lines = file.readlines() # read all lines
        batch_line = lines[1] # extract line 1
        batch_number_runnb = batch_line[15:] # Extract from 16 character to :
        batch_number, runnb= batch_number_runnb.split(':') # split into batch number and Run number
        batch_number_trim = batch_number.strip() # remmove space at both end
        runnb_trim = runnb.strip() # remove space at both end
        print('Batch Number is:', batch_number_trim, '\nRun Number is:', runnb_trim) # print both
        return batch_number_trim, runnb_trim
                        

def search_str(file_path, word):
    with open(file_path, 'r') as file:
        # read all lines in a file
        lines = file.readlines()
        for line in lines:
            # check if string present on a current line
                    if line.find(word) != -1:
                        print(word, 'string exists in file')
                        print('Line Number:', lines.index(line))
                        print('Line:', line)
                        
def lost_Master(file_path, deco):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(deco) != -1:
                print('\nWe have a lost of communication on Master with the basket Line Number:', lines.index(line))
                print('Here is the Line:', line)

def lost_Client(file_path, deco):
    if serial_client_1 == 0:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.find(deco) != -1:
                    print('\nWe have a lost of communication on Client with the basket Line Number:', lines.index(line))
                    print('Here is the Line:', line)

                
def start_Master(file_path, time_start_M):
    date_format = '%H:%M:%S'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(time_start_M) != -1:
                Test_Start_Master = line[:8]
                Test_Start_Master_s = int(line[:2]) * 3600 + int(line[3:5]) * 60 + int(line[6:8])
                Debut_Master = datetime.strptime(Test_Start_Master, date_format).time()
                print('\nTest Information Master')
                print('Test Time start is:', line[:12], 'aka', Debut_Master)
    return Test_Start_Master_s
                
def start_Client(file_path, time_start_C):
    date_format = '%H:%M:%S'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(time_start_C) != -1:
                Test_Start_Client = line[:8]
                Test_Start_Client_s = int(line[:2]) * 3600 + int(line[3:5]) * 60 + int(line[6:8])
                Debut_Client = datetime.strptime(Test_Start_Client, date_format).time()
                print('\nTest Information Client')
                print('Test Time start is:', line[:12], 'aka', Debut_Client)
    return Test_Start_Client_s
                
def end_Master(file_path, time_end_M):
    date_format = '%H:%M:%S'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(time_end_M) != -1:
                Test_End_Master = line[:8]
                Fin_Master = datetime.strptime(Test_End_Master, date_format).time()
                Test_End_Master_s = int(line[:2]) * 3600 + int(line[3:5]) * 60 + int(line[6:8])
                print('Test Time stop is:', line[:12], 'aka', Fin_Master)
    return Test_End_Master_s

def end_Client(file_path, time_end_C):
    date_format = '%H:%M:%S'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(time_end_C) != -1:
                Test_End_Client = line[:8]
                Fin_Client = datetime.strptime(Test_End_Client, date_format).time()
                Test_End_Client_s = int(line[:2]) * 3600 + int(line[3:5]) * 60 + int(line[6:8])
                print('Test Time stop is:', line[:12], 'aka', Fin_Client)
    return Test_End_Client_s
                
                
def Test_Duration_Master(Debut, Fin):
    duration_Master = Test_End_Master_s - Test_Start_Master_s
    print('Duration of the test is:', time.strftime("%H h %M min %S s", time.gmtime(duration_Master)))
    
def Test_Duration_Client(Debut, Fin):
    if Test_Start_Client_s == None or Test_End_Master_s == None:
        print('No Desintegration')
    else:
        duration_Client = Test_End_Client_s - Test_Start_Client_s
        print('Duration of the test is:', time.strftime("%H h %M min %S s", time.gmtime(duration_Client)))

#def desint_time_Master(file_path, basket_Master_info):
    #with open(file_path, 'r') as file:
        #lines = file.readlines()
        #for line in lines:
            #if line.find(basket_Master_info) != -1:
                #Time_Pos_1 = Line[]
        
def Manual_End(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find('Test manually finished.') != -1:
                print('\nTest was manually ended at line :', lines.index(line))
                print('Here is the Line:', line)
                 
                

driver_version(TEXT_FILE)

Batch_Run(TEXT_FILE)
               
serial_master(TEXT_FILE, '!GETSNR 1')

serial_client_1(TEXT_FILE, '!GETSNR 2')

Manual_End(TEXT_FILE)    

Test_Start_Master_s = start_Master(TEXT_FILE, ':SETSTA 1 1')
Test_End_Master_s = end_Master(TEXT_FILE, ':SETSTA 1 0')
Test_Duration_Master(Test_Start_Master_s, Test_End_Master_s)

Test_Start_Client_s = start_Client(TEXT_FILE, ':SETSTA 2 1')
Test_End_Client_s = end_Client(TEXT_FILE, ':SETSTA 2 0')
Test_Duration_Client(Test_Start_Client_s, Test_End_Client_s)
            
lost_Master(TEXT_FILE, 'FULL 0 1')

lost_Client(TEXT_FILE, 'FULL 0 2')

