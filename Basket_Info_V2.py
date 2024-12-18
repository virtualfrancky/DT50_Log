from decimal import Decimal
import re
import time
from pathlib import Path

ROOT_DIR = Path.cwd()
F_Log = input('Please type the Log file with .txt at the end : \n')
TEXT_FILE = ROOT_DIR / F_Log
#TEXT_FILE = ROOT_DIR / 'DT50_Log.txt'


def serial_Basket_Master(file_path, SRN_B_M):
    list_lines_B_M = []
    with open(file_path, 'r') as file:
        lines_B_M = file.readlines()
        for line_B_M in lines_B_M:
            if line_B_M.find(SRN_B_M) != -1:
                list_lines_B_M.append(line_B_M)
                serial_B_Master = list_lines_B_M[-1]
        serial_B_Master = serial_B_Master.rstrip()
        serial_B_Master = serial_B_Master[:-8]
        serial_B_Master = serial_B_Master[25:]
        print('Serial Number of Master Basket is :', serial_B_Master)
    return SRN_B_M
        
def serial_Basket_Client(file_path, SRN_B_C):
    list_lines_B_C = []
    with open(file_path, 'r') as file:
        lines_B_C = file.readlines()
        for line_B_C in lines_B_C:
            if line_B_C.find(SRN_B_C) != -1:
                list_lines_B_C.append(line_B_C)
                serial_B_Client = list_lines_B_C[-1]
        serial_B_Client = serial_B_Client.rstrip()
        serial_B_Client = serial_B_Client[:-8]
        serial_B_Client = serial_B_Client[25:]
        print('Serial Number of Client Basket is :',serial_B_Client)
    return SRN_B_C

def desint_time_Master(file_path, basket_Master_info):
    list_lines = []                                                         # list is emptied
    list_lines_B_M = []                                                     # list is emptied
    with open(file_path, 'r') as file:                                      # open the file
        lines = file.readlines()                                            # read each line
        for line in lines:                                                  # for each line of lines
            if line.find(basket_Master_info) != -1:                         # look if the line contains '!STS 1 BASKET'
                list_lines.append(line)                                     # add the line to the list
                line_basket = list_lines[-1]                                # put the list item of list in variable line_basket
        line_basket = line_basket.rstrip()                                  # trim space at the end
        line_basket = line_basket[:-8]                                      # trim last 8 characters
        line_basket = line_basket[29:]                                      #trim 1st 29th characters
        basket_v1_M, basket_v2_M, basket_v3_M, basket_v4_M, basket_v5_M, basket_v6_M, basket_v7_M, basket_v8_M, basket_v9_M = 0, 0, 0, 0, 0, 0, 0, 0, 0       # put all variables to 0
        list_v = line_basket.split()                                                                                                        # split all element and put them into a list called list_v
        basket_v1_M, basket_v2_M, basket_v3_M, basket_v4_M, basket_v5_M, basket_v6_M, basket_v7_M, basket_v8_M, basket_v9_M = [list_v[i] for i in (0, 1, 2, 3, 4, 5, 6, 7, 8)]    # assign each element to a variable
        basket_v1_M = int(basket_v1_M)
        basket_v2_M = int(basket_v2_M)
        basket_v3_M = int(basket_v3_M)
        basket_v4_M = int(basket_v4_M)
        basket_v5_M = int(basket_v5_M)
        basket_v6_M = int(basket_v6_M)
        basket_v7_M = int(basket_v7_M)
        basket_v8_M = int(basket_v8_M)
        basket_v9_M = float(basket_v9_M)
        #print(line_basket)
    return basket_v1_M, basket_v2_M, basket_v3_M, basket_v4_M, basket_v5_M, basket_v6_M, basket_v7_M, basket_v8_M, basket_v9_M

def desint_time_Client(file_path, basket_Client_info):
    list_lines = []                                                         # list is emptied
    list_lines_B_C = []                                                     # list is emptied
    with open(file_path, 'r') as file:                                      # open the file
        lines = file.readlines()                                            # read each line
        for line in lines:                                                  # for each line of lines
            if line.find(basket_Client_info) != -1:                         # look if the line contains '!STS 2 BASKET'
                list_lines.append(line)                                     # add the line to the list
                line_basket = list_lines[-1]                                # put the list item of list in variable line_basket
        line_basket = line_basket.rstrip()                                  # trim space at the end
        line_basket = line_basket[:-8]                                      # trim last 8 characters
        line_basket = line_basket[29:]                                      #trim 1st 29th characters
        basket_v1_C, basket_v2_C, basket_v3_C, basket_v4_C, basket_v5_C, basket_v6_C, basket_v7_C, basket_v8_C, basket_v9_C = 0, 0, 0, 0, 0, 0, 0, 0, 0       # put all variables to 0
        list_v = line_basket.split()                                                                                                        # split all element and put them into a list called list_v
        basket_v1_C, basket_v2_C, basket_v3_C, basket_v4_C, basket_v5_C, basket_v6_C, basket_v_C, basket_v8_C, basket_v9_C = [list_v[i] for i in (0, 1, 2, 3, 4, 5, 6, 7, 8)]    # assign each element to a variable
        basket_v1_C = int(basket_v1_C)
        basket_v2_C = int(basket_v2_C)
        basket_v3_C = int(basket_v3_C)
        basket_v4_C = int(basket_v4_C)
        basket_v5_C = int(basket_v5_C)
        basket_v6_C = int(basket_v6_C)
        basket_v7_C = int(basket_v7_C)
        basket_v8_C = int(basket_v8_C)
        basket_v9_C = float(basket_v9_C)        
        #print(line_basket)
    return basket_v1_C, basket_v2_C, basket_v3_C, basket_v4_C, basket_v5_C, basket_v6_C, basket_v7_C, basket_v8_C, basket_v9_C

def basket_explanation_Master(basket_v1_M, basket_v2_M, basket_v3_M, basket_v4_M, basket_v5_M, basket_v6_M, basket_v7_M, basket_v8_M, basket_v9_M):
    # 1st number Type of Basket
    # print(basket_v1_M)
    # print(basket_v2_M)
    print('\n')
    print('Info Basket Master')
    serial_Basket_Master(TEXT_FILE, '!GETBSN 1')
    if basket_v1_M == 0:
        print('No Basket connected')
    elif basket_v1_M == 1:
        print('6 postions Basket')
    elif basket_v1_M == 2:
        print('3 positions Basket')
    elif basket_v1_M == -1:
        print('Incompatible Basket Firmware')
    else:
        print('Incompatible Mounting Firmware')
    # 2nd Number Type of detection Bin
    if basket_v1_M == 1:
        bin_val_Master = bin(basket_v2_M)
        bin_val_Master = bin_val_Master[2:]
        bin_val_Master = int(bin_val_Master)
        bin_val_Master = format(bin_val_Master, '018')
        # analyze by cell
        # create a new list with result for each cell
        cell_1, cell_2, cell_3, cell_4, cell_5, cell_6 = [bin_val_Master_G3[j] for j in (0, 1, 2, 3, 4, 5)]
        # cell triggered time
        print('\n')
        print('Information Cell 1:')
        if cell_1 == '000':
            print('No Detection')
        elif cell_1 == '010':
            print('Manual Detection at', basket_v3_M, 's')
        else:
            print('Automatic Detection at', basket_v3_M, 's')
        print('\n')
        print('Information Cell 2:')
        if cell_2 == '000':
            print('No Detection')
        elif cell_2 == '010':
            print('Manual Detection at', basket_v4_M, 's')
        else:
            print('Automatic Detection at', basket_v4_M, 's')
        print('\n')
        print('Information Cell 3:')
        if cell_3 == '000':
            print('No Detection')
        elif cell_3 == '010':
            print('Manual Detection at', basket_v5_M, 's')
        else:
            print('Automatic Detection at', basket_v5_M, 's')
        print('\n')
        print('Information Cell 4:')
        if cell_4 == '000':
            print('No Detection')
        elif cell_4 == '010':
            print('Manual Detection at', basket_v6_M, 's')
        else:
            print('Automatic Detection at', basket_v6_M, 's')
        print('\n')
        print('Information Cell 5:')
        if cell_5 == '000':
            print('No Detection')
        elif cell_5 == '010':
            print('Manual Detection at', basket_v7_M, 's')
        else:
            print('Automatic Detection at', basket_v7_M, 's')
        print('\n')
        print('Information Cell 6:')
        if cell_6 == '000':
            print('No Detection')
        elif cell_6 == '010':
            print('Manual Detection at', basket_v8_M, 's')
        else:
            print('Automatic Detection at', basket_v8_M, 's')        
    else:
        bin_val_Master = bin(basket_v2_M)
        bin_val_Master = bin_val_Master[2:]
        bin_val_Master = int(bin_val_Master)
        bin_val_Master = format(bin_val_Master, '09')        
    # separate by group of 3
    bin_val_Master_G3 = [bin_val_Master[i:i+3] for i in range(0, len(bin_val_Master), 3)]
    # print(bin_val_Master_G3)
    # analyze by cell
    # create a new list with result for each cell
    cell_1, cell_2, cell_3 = [bin_val_Master_G3[j] for j in (0, 1, 2)]
    # cell triggered time
    print('\n')
    print('Information Cell 1:')
    if cell_1 == '000':
        print('No Detection')
    elif cell_1 == '010':
        print('Manual Detection at', basket_v3_C, 's')
    else:
        print('Automatic Detection at', basket_v3_C, 's')
    print('\n')
    print('Information Cell 2:')
    if cell_2 == '000':
        print('No Detection')
    elif cell_2 == '010':
        print('Manual Detection at', basket_v4_C, 's')
    else:
        print('Automatic Detection at', basket_v4_C, 's')
    print('\n')
    print('Information Cell 3:')
    if cell_3 == '000':
        print('No Detection')
    elif cell_3 == '010':
        print('Manual Detection at', basket_v5_C, 's')
    else:
        print('Automatic Detection at', basket_v5_C, 's')
    print('\n')    
    
def basket_explanation_Client(basket_v1_C, basket_v2_C, basket_v3_C, basket_v4_C, basket_v5_C, basket_v6_C, basket_v7_C, basket_v8_C, basket_v9_C):
    # 1st number Type of Basket
    # print(basket_v1_C)
    # print(basket_v2_C)
    print('\n')
    print('Info Basket Client')
    serial_Basket_Client(TEXT_FILE, '!GETBSN 2')
    if basket_v1_C == 0:
        print('No Basket connected')
    elif basket_v1_C == 1:
        print('6 postions Basket')
    elif basket_v1_C == 2:
        print('3 positions Basket')
    elif basket_v1_C == -1:
        print('Incompatible Basket Firmware')
    else:
        print('Incompatible Mounting Firmware')
    # 2nd Number Type of detection Bin
    if basket_v1_C == 1:
        bin_val_Client = bin(basket_v2_C)
        bin_val_Client = bin_val_Client[2:]
        bin_val_Client = int(bin_val_Client)
        bin_val_Client = format(bin_val_Client, '018')
        # analyze by cell
        # create a new list with result for each cell
        cell_1, cell_2, cell_3, cell_4, cell_5, cell_6 = [bin_val_Client_G3[j] for j in (0, 1, 2, 3, 4, 5)]
        # cell triggered time
        print('\n')
        print('Information Cell 1:')
        if cell_1 == '000':
            print('No Detection')
        elif cell_1 == '010':
            print('Manual Detection at', basket_v3_C, 's')
        else:
            print('Automatic Detection at', basket_v3_C, 's')
        print('\n')
        print('Information Cell 2:')
        if cell_2 == '000':
            print('No Detection')
        elif cell_2 == '010':
            print('Manual Detection at', basket_v4_C, 's')
        else:
            print('Automatic Detection at', basket_v4_C, 's')
        print('\n')
        print('Information Cell 3:')
        if cell_3 == '000':
            print('No Detection')
        elif cell_3 == '010':
            print('Manual Detection at', basket_v5_C, 's')
        else:
            print('Automatic Detection at', basket_v5_C, 's')
        print('\n')
        print('Information Cell 4:')
        if cell_4 == '000':
            print('No Detection')
        elif cell_4 == '010':
            print('Manual Detection at', basket_v6_C, 's')
        else:
            print('Automatic Detection at', basket_v6_C, 's')
        print('\n')
        print('Information Cell 5:')
        if cell_5 == '000':
            print('No Detection')
        elif cell_5 == '010':
            print('Manual Detection at', basket_v7_C, 's')
        else:
            print('Automatic Detection at', basket_v7_C, 's')
        print('\n')
        print('Information Cell 6:')
        if cell_6 == '000':
            print('No Detection')
        elif cell_6 == '010':
            print('Manual Detection at', basket_v8_C, 's')
        else:
            print('Automatic Detection at', basket_v8_C, 's')        
    else:
        bin_val_Client = bin(basket_v2_C)
        bin_val_Client = bin_val_Client[2:]
        bin_val_Client = int(bin_val_Client)
        bin_val_Client = format(bin_val_Client, '09')        
    # separate by group of 3
    bin_val_Client_G3 = [bin_val_Client[i:i+3] for i in range(0, len(bin_val_Client), 3)]
    # print(bin_val_Client_G3)
    # analyze by cell
    # create a new list with result for each cell
    cell_1, cell_2, cell_3 = [bin_val_Client_G3[j] for j in (0, 1, 2)]
    # cell triggered time
    print('\n')
    print('Information Cell 1:')
    if cell_1 == '000':
        print('No Detection')
    elif cell_1 == '010':
        print('Manual Detection at', basket_v3_C, 's', '(', time.strftime("%H h %M min %S s", time.gmtime(basket_v3_C)), ')')
    else:
        print('Automatic Detection at', basket_v3_C, 's', '(', time.strftime("%H h %M min %S s", time.gmtime(basket_v3_C)), ')')
    print('\n')
    print('Information Cell 2:')
    if cell_2 == '000':
        print('No Detection')
    elif cell_2 == '010':
        print('Manual Detection at', basket_v4_C, 's', '(', time.strftime("%H h %M min %S s", time.gmtime(basket_v4_C)), ')')
    else:
        print('Automatic Detection at', basket_v4_C, 's', '(', time.strftime("%H h %M min %S s", time.gmtime(basket_v4_C)), ')')
    print('\n')
    print('Information Cell 3:')
    if cell_3 == '000':
        print('No Detection')
    elif cell_3 == '010':
        print('Manual Detection at', basket_v5_C, 's', '(', time.strftime("%H h %M min %S s", time.gmtime(basket_v5_C)), ')')
    else:
        print('Automatic Detection at', basket_v5_C, 's', '(', time.strftime("%H h %M min %S s", time.gmtime(basket_v5_C)), ')')
    print('\n')

            
basket_v1_M, basket_v2_M, basket_v3_M, basket_v4_M, basket_v5_M, basket_v6_M, basket_v7_M, basket_v8_M, basket_v9_M = desint_time_Master(TEXT_FILE, '!STS 1 BASKET')
basket_v1_C, basket_v2_C, basket_v3_C, basket_v4_C, basket_v5_C, basket_v6_C, basket_v7_C, basket_v8_C, basket_v9_C = desint_time_Client(TEXT_FILE, '!STS 2 BASKET')
basket_explanation_Master(basket_v1_M, basket_v2_M, basket_v3_M, basket_v4_M, basket_v5_M, basket_v6_M, basket_v7_M, basket_v8_M, basket_v9_M)
basket_explanation_Client(basket_v1_C, basket_v2_C, basket_v3_C, basket_v4_C, basket_v5_C, basket_v6_C, basket_v7_C, basket_v8_C, basket_v9_C)