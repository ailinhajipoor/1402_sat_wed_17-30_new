f = open("info.txt", "r")  # read
# data = f.read() str
data = f.readlines()  # list
f.close()

# print(data)
print(type(data))
print(data[2].strip("\n"))
print(data[2])
# strip
