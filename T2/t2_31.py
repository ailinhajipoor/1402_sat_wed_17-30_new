print("\n\n\n\n----------------------- welcome -----------------------\n\n\n\n")
print("Drink Menu: \n")
print("Soda  ----- 10$")
print("Water ----- 5 $")

print("\nFood Menu: \n")
print("Hotdog  ----- 10$")
print("Pizza   ----- 25$")
print("Cheese   ----- 25$")

print("\n Dessert Menu: \n")
print("Jelly  ----- 10$")
print("Latte  ----- 25$")
print("Cheese Cake  ----- 25$\n\n")

all_data = []
price = 0
while True :
    Food = input("Food : " )
    
    if Food !="finish":
        if Food == "Hotdog":
            price = price +10
            all_data.append(Food)
        elif Food == "Pizza":
            price = price +25
            all_data.append(Food)
        elif Food == "Cheese":
            price = price +25
            all_data.append(Food)
        else:
            print("type clearly plz.")
    else:
        break
    
    
Drink = input("Drink : " )
Dessert = input("Dessert : " )

all_data.append(Drink)
all_data.append(Dessert)

f = open("order.txt","w")

for item in all_data:
    f.write(item+"\n")
f.write("total price : " + str(price) )
    
f.close()