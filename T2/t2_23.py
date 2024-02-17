import turtle
fav_colors = []
for i in range(6):
    color = input("color : ")
    fav_colors.append(color)

#-----------1 ---------------------
print(fav_colors)
for i in range(0,6):
    turtle.pencolor(fav_colors[i])
    turtle.circle(100)
    turtle.left(60)
    

turtle.done()