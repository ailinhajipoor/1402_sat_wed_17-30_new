t= 100
turn = 0

while True :
    number = int(input("type number : "))
    t = t - number
    turn = turn +1 
    if turn == 5 :
        break
print(t)