from os import system
from time import sleep
f = open("fishh.txt","a")
food=["burger","pizza","hotdog","kapak"]
prise=["$1","$2","$3","$4"]
for i in range(4):
    print(food[i],prise[i])
yourfish=[]
while True:
    your_food=input("wich do you want?: ")
    if your_food== "finish":
        break
    yourfish.append (your_food)
pris=(0)
pris2=(0)
while True:
    if len(yourfish)==0:
        break
    a = int(yourfish.count (yourfish[0]))
    b = (yourfish[0])
    if b == "burger":
        pris=pris+ 1*a
        pris2=1*a
        f.write(f"{a}{b} = {pris2}")
        f.write("\n")
    elif b == "pizza":
        pris=pris+ 2*a
        pris2=pris2=2*a
        f.write(f"{a}{b} = {pris2}")
        f.write("\n")
    elif b == "hotdog":
        pris=pris+ 3*a
        pris2=3*a
        f.write(f"{a}{b} = {pris2}")
        f.write("\n")
    elif b == "kapak":
        pris=pris+ 4*a
        pris2=4*a
        f.write(f"{a}{b} = {pris2}")
        f.write("\n")
    elif b != "kapak" or "hotdog" or "pizza" or "burger":
        print(f"{b} not suported")
        break
    for i in range(a):
        yourfish.remove(b)
f.write(f"all = {pris}")
f.close()