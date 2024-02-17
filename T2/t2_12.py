total = 0 
turn = 0
while True:
    number = int(input("type number : "))
    total = total +number
    turn = turn +1 
    if turn==4 :
        break
print(total)