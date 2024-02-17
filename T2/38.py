print("\n\n\n----------- Welcome To SIMORGH Hotel -----------\n\n\n")
print("Reservation - Coffe Shop - Restaurant")
r = {
    "yeknafare": 1000000,
    "chandnafare": 3000000,
    "small soit": 5000000,
    "big soit": 6000000,
    "small room with serv food": 7000000,
    "big room with serv food": 9000000,
}

y = []
mony = 0

while True :
    s = input("What do you want ? ")
    if s == "Finish":
        print("end")
        break
    elif s == "Reservation":
        for i, z in r.items():
            print(i, z)
        n = input("Chose a room : ")
        if n == "yeknafare":
            mony = mony + 1000000
            y.append(n)
        elif n == "chandnafare":
            mony = mony + 3000000
            y.append(n)
        elif n == "small soit":
            mony = mony + 5000000
            y.append(n)
        elif n == "big soit":
            mony = mony + 6000000
            y.append(n)
        elif n == "small room with serv food":
            mony = mony + 7000000
            y.append(n)
        elif n == "big room with serv food":
            mony = mony + 9000000
            y.append(n)
    elif s == "Coffe Shop":
        coffe_menu = {
                "tea": 10000,
                "caffe": 15000,
                "late": 20000,
                "hot chocolate": 30000,
                "cake": 40000,
                "chese cake": 45000,
                "milk sheik": 50000,
                "aispack": 60000,
                "pancake": 65000,
                "caca": 70000,
            }
        for i, z in coffe_menu.items():
            print(i, z)
        o = input("What do you want ? ")
        if o == "tea":
            mony = mony + 10000
            y.append(o)
        elif o == "caffe":
            mony = mony + 15000
            y.append(o)
        elif o == "late":
            mony = mony + 20000
            y.append(o)
        elif o == "hot chocolate":
            mony = mony + 30000
            y.append(o)
        elif o == "cake":
            mony = mony + 40000
            y.append(o)
        elif o == "chese cake":
            mony = mony + 45000
            y.append(o)
        elif o == "milk sheik":
            mony = mony + 50000
            y.append(o)
        elif o == "aispack":
            mony = mony + 60000
            y.append(o)
        elif o == "pancake":
            mony = mony + 65000
            y.append(o)
        elif o == "caca":
            mony = mony + 70000
            y.append(o)





    elif s == "Restaurant":
        print("\nPish gaza : \n")
        {
            "soup go": 40000,
            "soup rshte": 50000,
            "ashe torsh": 60000,
            "ashe reshte": 70000,
            "ashe dogh": 65000,
            "ashe ghalamkar": 80000,
            "sibzamini sorkh shode": 90000,
            "gharch sokharii": 95000,
        }

        m = input("What do you want ? ")
        if m == "soup go":
            mony = mony + 40000
            y.append(m)
        elif m == "soup reshte":
            mony = mony + 50000
            y.append(m)
        elif m == "soup torsh":
            mony = mony + 60000
            y.append(m)
        elif m == "ashe reshte":
            mony = mony + 70000
            y.append(m)
        elif m == "ashe dogh":
            mony = mony + 65000
            y.append(m)
        elif m == "ashe ghalamkar":
            mony = mony + 80000
            y.append(m)
        elif m == "sobzamini sorkh shde":
            mony = mony + 90000
            y.append(m)
        elif m == "gharch sokharii":
            mony = mony + 95000
            y.append(m)

        print("\nghazay asly : \n")
        {
            "pizza makhsos": 100000,
            "pizza peperony": 200000,
            "pizza ghosht va ghach": 250000,
            "hotdog": 180000,
            "chelo kabab": 300000,
            "chelo goge": 350000,
            "chelo gosht": 400000,
            "pasta": 380000,
        }

        x = input("What do you want ? ")
        if x == "pizza makhsos":
            mony = mony + 100000
            y.append(x)
        elif x == "pizza peperony":
            mony = mony + 200000
            y.append(x)
        elif x == "pizza ghosht va gharch":
            mony = mony + 250000
            y.append(x)
        elif x == "hotdog":
            mony = mony + 180000
            y.append(x)
        elif x == "chelo kabab":
            mony = mony + 300000
            y.append(x)
        elif x == "chelo goge":
            mony = mony + 350000
            y.append(x)
        elif x == "chelo gosht":
            mony = mony + 400000
            y.append(x)
        elif x == "pasta":
            mony = mony + 380000
            y.append(x)

        print("\nDeser : \n")
        {
            "jally": 120000,
            "bastany ba mivehay ostovaii": 200000,
            "bastany": 150000,
            "reshte khoshkar": 180000,
        }

        q = input("What do you want ? ")
        if q == "jally":
            mony = mony + 120000
            y.append(q)
        elif q == "bastany ba mivehay ostovaii":
            mony = mony + 200000
            y.append(q)
        elif q == "bastany":
            mony = mony + 150000
            y.append(q)
        elif q == "reahte khishkar":
            mony = mony + 180000
            y.append(q)
    else:
        print("Type clearly please")
n = open("Hotel orders.py", "w")
n.write(str(a))
