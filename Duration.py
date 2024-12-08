import time
def Test_Duration_Client(Debut, Fin):
    if Test_Start_Client_s == None or Test_End_Master_s == None:
        print('No Desintegration')
    else:
        duration_Client = Test_End_Client_s - Test_Start_Client_s
        print('Duration of the test is:', time.strftime("%H h %M min %S s", time.gmtime(duration_Client)))
              

file_path = r'C:\Users\franc\Documents\Python\Franck\DT50_Log.txt'
  
Test_Duration_Client(Test_Start_Client_s, Test_End_Client_s)