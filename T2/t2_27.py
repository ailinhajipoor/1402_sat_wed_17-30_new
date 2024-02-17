a = ["red","orange","green","orange","blue","orange"]
a.append("black")

print(a)

b = a.count("orange")

for i in range(b):
    a.remove("orange") 
    
print(a)