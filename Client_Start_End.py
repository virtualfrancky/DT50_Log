from datetime import datetime
from pathlib import Path

ROOT_DIR = Path.cwd()
TEXT_FILE = ROOT_DIR / 'DT50_Log.txt'

def start_Client(file_path, time_start_C):
    date_format = '%H:%M:%S'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(time_start_C) != -1:
                Test_Start_Client = line[:8]
                Test_Start_Client_s = int(line[:2]) * 3600 + int(line[4:5]) * 60 + int(line[7:8])
                Debut_Client = datetime.strptime(Test_Start_Client, date_format).time()
                print('\nTest Information Client')
                print('Test Time start is:', line[:12], 'aka', Debut_Client)
    return Test_Start_Client_s

def end_Client(file_path, time_end_C):
    date_format = '%H:%M:%S'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(time_end_C) != -1:
                Test_End_Client = line[:8]
                Fin_Client = datetime.strptime(Test_End_Client, date_format).time()
                Test_End_Client_s = int(line[:2]) * 3600 + int(line[4:5]) * 60 + int(line[7:8])
                print('Test Time stop is:', line[:12], 'aka', Fin_Client)
    return Test_End_Client_s

Test_Start_Client_s = start_Client(TEXT_FILE, ':SETSTA 2 1')
Test_End_Client_s = end_Client(TEXT_FILE, ':SETSTA 2 0')