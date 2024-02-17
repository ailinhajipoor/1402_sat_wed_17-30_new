
#login  or register 
a = input("login or register :")
if a == "login":
    f = open("information.txt","r")
    data = f.readlines()
    username = data[0].strip("\n")
    password = data[1].strip("\n")
    us = input("username : ")
    if username == us:
        ps = input("password : ")
        if password == ps:
            print("welcome to your dashboard")
        else:
            print("plz type password correctly")
    else:
        print("incorrect username !")
        
elif a == "register":
    f = open("information.txt","w")
    us = input("username : ")
    ps = input("password : ")
    f.write(us+"\n")
    f.write(ps+"\n")
    f.close()
    
else:
    print("choose login or register")