names = []
phone_numbers = []
for i in range(5):
    print()
for i in range(5):
    n = input("name : ")
    names.append(n)
    p = input("phone number: ")
    phone_numbers.append(p)
print("================ Contact List ==================")
for i in range(5):
    print("--------------------------")
    print(names[i] + ":" + phone_numbers[i])

print("-----------------End Of List-------------------")
for i in range(5):
    print()
