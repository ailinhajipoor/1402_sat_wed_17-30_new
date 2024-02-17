# f = open("info.txt","w") #write -->replace
f = open("info.txt","a") #append -->last data saved  and add new items
f.write("ailin")
f.write("\n") #\n --> new line
f.write("yasna\nmoz")
f.close()