word = "!STS"
count = 0
file_path = 'C:\Users\franc\Documents\Python\Franck\DT50_Log.txt'
with open(file_path, 'r') as file: 
    for line in f: 
        words = line.split() 
        for i in words: 
            if(i==word): 
                count=count+1
print("Occurrences of the word", word, ":", count)