import os 
a = input("filename : ")
filename = a +".txt"
files = os.listdir()
print(files)
if filename in files :
    b = input("edit,show : ")
    if b =="edit":
        f = open(filename,"r")
        data = f.readlines()
        f.close()
        
        l1 = data[0]
        l2 = data[1]
        l3 = data[2]
        soal = input("tarikh?vasiat?ersalshode ya na?")
        if soal =="tarikh":
            tarikh = input("?")
            f = open(filename,"w")
            f.write(tarikh+"\n")
            f.write(l2)
            f.write(l3)
        elif soal =="vasiat":
            vasiat = input("?")
            f = open(filename,"w")
            f.write(l1)
            f.write(vasiat+"\n")
            f.write(l3)
    elif b=="show":
        f = open(filename,"r")
        data = f.read()
        print(data)
        
    
    
    
    
