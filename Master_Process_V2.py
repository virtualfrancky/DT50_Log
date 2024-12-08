from datetime import datetime
import time
from pathlib import Path
from file_read_backwards import FileReadBackwards


ROOT_DIR = Path.cwd()
F_Log = input('Please type the Log file with .txt at the end : \n')
TEXT_FILE = ROOT_DIR / F_Log
#TEXT_FILE = ROOT_DIR / 'DT50_Log.txt'

def Process_Master(file_path, STS_1) :
    list_pre_heat_M = []
    list_Master = []
    list_Ready = []
    list_Pre_Start = []
    list_Pre_Test = []
    list_Test = []
    lines_2 = []
    date_format = '%H:%M:%S'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(STS_1) != -1:
                list_Master.append(line)
            elif line.find(':SETSTA 1') != -1:
                list_Master.append(line)
        if list_Master == []:
            print('\n No Master used for this run.')
        else:
            print('\n List Process for Master:')
            #List for Master
            for item_P_H in list_Master:
                if item_P_H.find('4', 46, 48) != -1:
                    list_pre_heat_M.append(item_P_H)
                elif item_P_H.find(':SETSTA 1 2') != -1:
                    break
                elif item_P_H.find(':SETSTA 1 1') != -1:
                    break
            if list_pre_heat_M == []:
                print('- No Pre_Heat for this run.')
            else:
                #List for Pre Heat
                item_1 = list_pre_heat_M[0]
                item_1 = item_1.rstrip()
                item_1 = item_1[:8]
                item_1_s = datetime.strptime(item_1, date_format).time()
                item_1_s = int(item_1[:2]) * 3600 + int(item_1[3:5]) * 60 + int(item_1[6:8])
                item_2 = list_pre_heat_M[-1]
                item_2 = item_2.rstrip()
                item_2 = item_2[:8]
                item_2_s= datetime.strptime(item_2, date_format).time()
                item_2_s = int(item_2[:2]) * 3600 + int(item_2[3:5]) * 60 + int(item_2[6:8])
                duration_pre_h_M = item_2_s - item_1_s
                print('- Pre Heat phase for Master start at', item_1, 'and end at', item_2, 'for a duration of', time.strftime("%H h %M min %S s", time.gmtime(duration_pre_h_M)))
            #print(list_pre_heat_M)
            #list for Ready
            for item_Ready in list_Master:
                if item_Ready.find('0', 46, 48) != -1:
                    list_Ready.append(item_Ready)
                elif item_Ready.find(':SETSTA 1 2') != -1:
                    break
                elif item_Ready.find(':SETSTA 1 1') != -1:
                    break                
            item_3 = list_Ready[0]
            item_3 = item_3.rstrip()
            item_3 = item_3[:8]
            item_3_s = datetime.strptime(item_3, date_format).time()
            item_3_s = int(item_3[:2]) * 3600 + int(item_3[3:5]) * 60 + int(item_3[6:8])
            item_4 = list_Ready[-1]
            item_4 = item_4.rstrip()
            item_4 = item_4[:8]
            item_4_s= datetime.strptime(item_4, date_format).time()
            item_4_s = int(item_4[:2]) * 3600 + int(item_4[3:5]) * 60 + int(item_4[6:8])
            duration_Ready = item_4_s - item_3_s
            print('- Ready phase for Master start at', item_3, 'and end at', item_4, 'for a duration of', time.strftime("%H h %M min %S s", time.gmtime(duration_Ready)))
            #print(list_Ready)
            #list for Pre_Start
            for item_Pre_Start in list_Master:
                if item_Pre_Start.find('1', 46, 48) != -1:
                    list_Pre_Start.append(item_Pre_Start)
                elif item_Pre_Start.find(':SETSTA 1 0') != -1:
                    break            
            item_5 = list_Pre_Start[0]
            item_5 = item_5.rstrip()
            item_5 = item_5[:8]
            item_5_s = datetime.strptime(item_5, date_format).time()
            item_5_s = int(item_5[:2]) * 3600 + int(item_5[3:5]) * 60 + int(item_5[6:8])
            item_6 = list_Pre_Start[-1]
            item_6 = item_6.rstrip()
            item_6 = item_6[:8]
            item_6_s= datetime.strptime(item_6, date_format).time()
            item_6_s = int(item_6[:2]) * 3600 + int(item_6[3:5]) * 60 + int(item_6[6:8])
            duration_Pre_Start = item_6_s - item_5_s
            print('- Pre-Start phase for Master start at', item_5, 'and end at', item_6, 'for a duration of', time.strftime("%H h %M min %S s", time.gmtime(duration_Pre_Start)))
            #print(list_Pre_Start)
            #list for Pre_Test
            for item_Pre_Test in list_Master:
                if item_Pre_Start.find('2', 46, 48) == 0:
                    print('- There is no Pre-Test for this test')
                elif item_Pre_Test.find('2', 46, 48) != -1:
                    list_Pre_Test.append(item_Pre_Test)
                elif item_Pre_Test.find(':SETSTA 1 0') != -1:
                    break
            if list_Pre_Test == []:
                print('- No Pre-Test for this run')
            else:
                item_7 = list_Pre_Test[0]
                item_7 = item_7.rstrip()
                item_7 = item_7[:8]
                item_7_s = datetime.strptime(item_7, date_format).time()
                item_7_s = int(item_7[:2]) * 3600 + int(item_7[3:5]) * 60 + int(item_7[6:8])
                item_8 = list_Pre_Test[-1]
                item_8 = item_8.rstrip()
                item_8 = item_8[:8]
                item_8_s= datetime.strptime(item_8, date_format).time()
                item_8_s = int(item_8[:2]) * 3600 + int(item_8[3:5]) * 60 + int(item_8[6:8])
                duration_Pre_Test = item_8_s - item_7_s
                print('- Pre-Test phase for Master start at', item_7, 'and end at', item_8, 'for a duration of', time.strftime("%H h %M min %S s", time.gmtime(duration_Pre_Test)))
            #list for Test
            file = []
            list_Master = []
            lines = []
            lines_2 = []
            with FileReadBackwards(file_path, encoding="utf-8") as file:
                for lines in file:
                    lines_2.append(lines)
                for line in lines_2:
                    if line.find(STS_1) != -1:
                        list_Master.append(line)
                    elif line.find(':SETSTA 1 1') != -1:
                        list_Master.append(line)
                        break
            list_Master.sort()
            for item_Test in list_Master:
                if item_Test.find('2', 46, 48) != -1:
                    list_Test.append(item_Test)
                elif item_Test.find(':SETSTA 1 0') != -1:
                    break
            if len(list_Test) == 0:
                print('- There was an error during Pre Start Phase, the DT50 never sent the "in Test" command')
            else:
                item_9 = list_Test[0]
                item_9 = item_9.rstrip()
                item_9 = item_9[:8]
                item_9_s = datetime.strptime(item_9, date_format).time()
                item_9_s = int(item_9[:2]) * 3600 + int(item_9[3:5]) * 60 + int(item_9[6:8])
                item_10 = list_Test[-1]
                item_10 = item_10.rstrip()
                item_10 = item_10[:8]
                item_10_s= datetime.strptime(item_10, date_format).time()
                item_10_s = int(item_10[:2]) * 3600 + int(item_10[3:5]) * 60 + int(item_10[6:8])
                duration_Test = item_10_s - item_9_s
                print('- Test phase for Master start at', item_9, 'and end at', item_10, 'for a duration of', time.strftime("%H h %M min %S s", time.gmtime(duration_Test)))
            #print(list_Test)
    
def Process_Client(file_path, STS_2) :
    list_pre_heat_C = []
    list_Client = []
    list_Ready = []
    list_Pre_Start = []
    list_Pre_Test = []
    list_Test = []
    date_format = '%H:%M:%S'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find(STS_2) != -1:
                list_Client.append(line)
            elif line.find(':SETSTA 2') != -1:
                list_Client.append(line)            
        if list_Client == []:
            print('\n\n No Client used for this Run.')
        else:
            print('\nList Process for Client:')
            #List for Client
            for item_P_H in list_Client:
                if item_P_H.find('4', 46, 48) != -1:
                    list_pre_heat_C.append(item_P_H)
                elif item_P_H.find(':SETSTA 2 2') != -1:
                    break
                elif item_P_H.find(':SETSTA 2 1') != -1:
                    break
            if list_pre_heat_C == []:
                print('- No Pre-Heat for this run.')
            else:
                #List for Pre Heat
                item_1 = list_pre_heat_C[0]
                item_1 = item_1.rstrip()
                item_1 = item_1[:8]
                item_1_s = datetime.strptime(item_1, date_format).time()
                item_1_s = int(item_1[:2]) * 3600 + int(item_1[3:5]) * 60 + int(item_1[6:8])
                item_2 = list_pre_heat_C[-1]
                item_2 = item_2.rstrip()
                item_2 = item_2[:8]
                item_2_s= datetime.strptime(item_2, date_format).time()
                item_2_s = int(item_2[:2]) * 3600 + int(item_2[3:5]) * 60 + int(item_2[6:8])
                duration_pre_h_C = item_2_s - item_1_s
                print('- Pre Heat phase for Client start at', item_1, 'and end at', item_2, 'for a duration of', time.strftime("%H h %M min %S s", time.gmtime(duration_pre_h_C)))
            #print(list_pre_heat_C)
            #list for Ready
            for item_Ready in list_Client:
                if item_Ready.find('0', 46, 48) != -1:
                    list_Ready.append(item_Ready)
                elif item_Ready.find(':SETSTA 2 0') != -1:
                    break              
            item_3 = list_Ready[0]
            item_3 = item_3.rstrip()
            item_3 = item_3[:8]
            item_3_s = datetime.strptime(item_3, date_format).time()
            item_3_s = int(item_3[:2]) * 3600 + int(item_3[3:5]) * 60 + int(item_3[6:8])
            item_4 = list_Ready[-1]
            item_4 = item_4.rstrip()
            item_4 = item_4[:8]
            item_4_s= datetime.strptime(item_4, date_format).time()
            item_4_s = int(item_4[:2]) * 3600 + int(item_4[3:5]) * 60 + int(item_4[6:8])
            duration_Ready = item_4_s - item_3_s
            print('- Ready phase for Client start at', item_3, 'and end at', item_4, 'for a duration of', time.strftime("%H h %M min %S s", time.gmtime(duration_Ready)))
            #print(list_Ready)
            #list for Pre_Start
            for item_Pre_Start in list_Client:
                if item_Pre_Start.find('1', 46, 48) != -1:
                    list_Pre_Start.append(item_Pre_Start)
                elif item_Pre_Start.find(':SETSTA 2 0') != -1:
                    break              
            item_5 = list_Pre_Start[0]
            item_5 = item_5.rstrip()
            item_5 = item_5[:8]
            item_5_s = datetime.strptime(item_5, date_format).time()
            item_5_s = int(item_5[:2]) * 3600 + int(item_5[3:5]) * 60 + int(item_5[6:8])
            item_6 = list_Pre_Start[-1]
            item_6 = item_6.rstrip()
            item_6 = item_6[:8]
            item_6_s= datetime.strptime(item_6, date_format).time()
            item_6_s = int(item_6[:2]) * 3600 + int(item_6[3:5]) * 60 + int(item_6[6:8])
            duration_Pre_Start = item_6_s - item_5_s
            print('- Pre-Start phase for Client start at', item_5, 'and end at', item_6, 'for a duration of', time.strftime("%H h %M min %S s", time.gmtime(duration_Pre_Start)))
            #print(list_Pre_Start)
            #list for Pre_Test
            for item_Pre_Test in list_Client:
                if item_Pre_Start.find('2', 46, 48) == 0:
                    print('- There is no Pre-Test for this test')        
                elif item_Pre_Test.find('2', 46, 48) != -1:
                    list_Pre_Test.append(item_Pre_Test)
                elif item_Pre_Test.find(':SETSTA 2 0') != -1:
                    break
            if list_Pre_Test == []:
                print('- No Pre-Test for this run')
            else:
                item_7 = list_Pre_Test[0]
                item_7 = item_7.rstrip()
                item_7 = item_7[:8]
                item_7_s = datetime.strptime(item_7, date_format).time()
                item_7_s = int(item_7[:2]) * 3600 + int(item_7[3:5]) * 60 + int(item_7[6:8])
                item_8 = list_Pre_Test[-1]
                item_8 = item_8.rstrip()
                item_8 = item_8[:8]
                item_8_s= datetime.strptime(item_8, date_format).time()
                item_8_s = int(item_8[:2]) * 3600 + int(item_8[3:5]) * 60 + int(item_8[6:8])
                duration_Pre_Test = item_8_s - item_7_s
                print('- Pre-Test phase for Client start at', item_7, 'and end at', item_8, 'for a duration of', time.strftime("%H h %M min %S s", time.gmtime(duration_Pre_Test)))    
            #list for Test
            file = []
            list_Client = []
            lines = []
            lines_2 = []
            with FileReadBackwards(file_path, encoding="utf-8") as file:
                for lines in file:
                    lines_2.append(lines)
                for line in lines_2:
                    if line.find(STS_2) != -1:
                        list_Client.append(line)
                    elif line.find(':SETSTA 2 1') != -1:
                        list_Client.append(line)
                        break
            list_Client.sort()            
            for item_Test in list_Client:
                if item_Test.find('2', 46, 48) != -1:
                    list_Test.append(item_Test)
            if len(list_Test) == 0:
                print('- There was an error during Pre Start Phase, the DT50 never sent the "in Test" command')
            else:
                item_9 = list_Test[0]
                item_9 = item_9.rstrip()
                item_9 = item_9[:8]
                item_9_s = datetime.strptime(item_9, date_format).time()
                item_9_s = int(item_9[:2]) * 3600 + int(item_9[3:5]) * 60 + int(item_9[6:8])
                item_10 = list_Test[-1]
                item_10 = item_10.rstrip()
                item_10 = item_10[:8]
                item_10_s= datetime.strptime(item_10, date_format).time()
                item_10_s = int(item_10[:2]) * 3600 + int(item_10[3:5]) * 60 + int(item_10[6:8])
                duration_Test = item_10_s - item_9_s
                print('- Test phase for Client start at', item_9, 'and end at', item_10, 'for a duration of', time.strftime("%H h %M min %S s", time.gmtime(duration_Test)))
            #print(list_Test)
  

Process_Master(TEXT_FILE, '!STS 1 FULL')
Process_Client(TEXT_FILE, '!STS 2 FULL')