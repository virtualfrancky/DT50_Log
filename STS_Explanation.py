from decimal import Decimal
import time

def line():
    line_STS = input('Copy the Line\n')
    return line_STS


def STS_Split(line_STS):
    line_STS_list = []
    line_STS = line_STS[:-8]
    line_STS_1 = line_STS.replace('<', '')
    line_STS_2 = line_STS_1.replace('FULL', '')
    line_STS_3 = line_STS_2.replace('!STS', '')
    line_STS_list = line_STS_3.split()
    Time, Device, Basket_Detection, Beaker_Detection, Temperature, Temp_Stat, Heater_STS, Temperate_STS, Error_Detection, System_STS, Run_Time, Cell_STS, Client_STS = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0
    Time, Device, Basket_Detection, Beaker_Detection, Temperature, Temp_Stat, Heater_STS, Temperate_STS, Error_Detection, System_STS, Run_Time, Cell_STS, Client_STS = [line_STS_list[i] for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)]
    Device = Device[0:2]
    Device = int(Device)
    Basket_Detection = int(Basket_Detection)
    Beaker_Detection = int(Beaker_Detection)
    Temperature = float(Temperature)
    Temp_Stat = float(Temp_Stat)
    Heater_STS = int(Heater_STS)
    Temperate_STS = int(Temperate_STS)
    Error_Detection = int(Error_Detection)
    System_STS = int(System_STS)
    Run_Time = int(Run_Time)
    Cell_STS = int(Cell_STS)
    Client_STS = int(Client_STS)
    #print(line_STS_list)
    return Time, Device, Basket_Detection, Beaker_Detection, Temperature, Temp_Stat, Heater_STS, Temperate_STS, Error_Detection, System_STS, Run_Time, Cell_STS, Client_STS
    
    

def STS_Explanation(Time, Device, Basket_Detection, Beaker_Detection, Temperature, Temp_Stat, Heater_STS, Temperate_STS, Error_Detection, System_STS, Run_Time, Cell_STS, Client_STS):
    #Time
    print(Time)
    #Device
    if Device == 1:
        print ('Master')
    else:
        print ('Client')
    #Basket_Detection
    if Basket_Detection == 0:
        print('No Basket connected')
    elif Basket_Detection == 1:
        print('6 postions Basket')
    elif Basket_Detection == 2:
        print('3 positions Basket')
    elif Basket_Detection == -1:
        print('Incompatible Basket Firmware')
    else:
        print('Incompatible Mounting Firmware')
    #Beaker_Detection
    if Beaker_Detection == 1:
        print('Beaker detected')
    else:
        print('Beaker not detected')
    #Temperature
    print('Temperature is:', Temperature)
    #Heater Status
    if Heater_STS == 1:
        print('heater is ON')
    else:
        print('Heater is OFF')
    #Temperate Status
    if Temperate_STS == 1:
        print('System is temperated')
    else:
        print('System is not temperated yet')
    #Error Detection
    if Error_Detection == 0:
        print('No error detected')
    else:
        print('Error detected')
    #System Status
    if System_STS == 0:
        print('System is idled')
    elif System_STS == 1:
        print('System is in move in test')
    elif System_STS == 2:
        print('System is in test')
    elif System_STS == 3:
        print('System move out of test')
    elif System_STS == 4:
        print('System is no reday for test')
    elif System_STS == 5:
        print('Test move in hold')
    elif System_STS == 6:
        print('Test is in hold')
    elif System_STS == 7:
        print('Test move out of hold')
    #run time
    print('Run time is', Run_Time, 's or', time.strftime("%H h %M min %S s", time.gmtime(Run_Time)))
    #Cell Status
    bin_val_list = []
    if Basket_Detection == 1:
        bin_val = bin(Cell_STS)
        bin_val = bin_val[2:]
        bin_val = int(bin_val)
        bin_val = format(bin_val, '018')
        # analyze by cell
        # create a new list with result for each cell
        cell_1, cell_2, cell_3, cell_4, cell_5, cell_6 = [bin_val[j] for j in (0, 1, 2, 3, 4, 5)]
        # cell triggered time
        print('\n')
        print('Information Cell 1:')
        if cell_1 == '000':
            print('No Detection')
        elif cell_1 == '010':
            print('Manual Detection')
        else:
            print('Automatic Detection')
        print('\n')
        print('Information Cell 2:')
        if cell_2 == '000':
            print('No Detection')
        elif cell_2 == '010':
            print('Manual Detection')
        else:
            print('Automatic Detection')
        print('\n')
        print('Information Cell 3:')
        if cell_3 == '000':
            print('No Detection')
        elif cell_3 == '010':
            print('Manual Detection')
        else:
            print('Automatic Detection')
        print('\n')
        print('Information Cell 4:')
        if cell_4 == '000':
            print('No Detection')
        elif cell_4 == '010':
            print('Manual Detection')
        else:
            print('Automatic Detection')
        print('\n')
        print('Information Cell 5:')
        if cell_5 == '000':
            print('No Detection')
        elif cell_5 == '010':
            print('Manual Detection')
        else:
            print('Automatic Detection')
        print('\n')
        print('Information Cell 6:')
        if cell_6 == '000':
            print('No Detection')
        elif cell_6 == '010':
            print('Manual Detection')
        else:
            print('Automatic Detection')        
    else:
        bin_val = bin(Cell_STS)
        bin_val = bin_val[2:]
        bin_val = int(bin_val)
        bin_val = format(bin_val, '09')
    # separate by group of 3
    bin_val_G3 = [bin_val[i:i+3] for i in range(0, len(bin_val), 3)]
    # print(bin_val_Client_G3)
    # analyze by cell
    # create a new list with result for each cell
    cell_1, cell_2, cell_3 = [bin_val_G3[j] for j in (0, 1, 2)]
    # cell triggered time
    print('\n')
    print('Information Cell 1:')
    if cell_1 == '000':
        print('No Detection')
    elif cell_1 == '010':
        print('Manual Detection')
    else:
        print('Automatic Detection')
    print('\n')
    print('Information Cell 2:')
    if cell_2 == '000':
        print('No Detection')
    elif cell_2 == '010':
        print('Manual Detection')
    else:
        print('Automatic Detection')
    print('\n')
    print('Information Cell 3:')
    if cell_3 == '000':
        print('No Detection')
    elif cell_3 == '010':
        print('Manual Detection')
    else:
        print('Automatic Detection')
    print('\n')    
    

line_STS = line()
Time, Device, Basket_Detection, Beaker_Detection, Temperature, Temp_Stat, Heater_STS, Temperate_STS, Error_Detection, System_STS, Run_Time, Cell_STS, Client_STS = STS_Split(line_STS)
STS_Explanation(Time, Device, Basket_Detection, Beaker_Detection, Temperature, Temp_Stat, Heater_STS, Temperate_STS, Error_Detection, System_STS, Run_Time, Cell_STS, Client_STS)