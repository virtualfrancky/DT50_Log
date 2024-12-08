def Manual_End(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.find('Test manually finished.') != -1:
                print('\nTest was manually ended at line :', lines.index(line))
                print('Here is the Line:', line)
                
                
file_path = r'C:\Users\franc\Documents\Python\Franck\DT50_Log.txt'
            
Manual_End(file_path)