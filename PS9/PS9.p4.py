def Ftrainticket(miles):
    if miles > 29:
        price = 12 * miles
    elif miles > 19:
        price = 10 * miles
    elif miles > 9:
        price = 8 * miles
    else:
        price = 5 * miles
    return price

# MAIN
ttprice = 0
r = input("Do you want to run the program? (y/n): ")
while r == 'y':
    last_name = input("Enter your last name: ")
    miles = int(input("Enter the number of miles from downtown Chicago: "))
    tickprice = Ftrainticket(miles)
    print("The price of the train ticket is $", tickprice)
    ttprice = ttprice + tickprice
    r = input("Do you want to run the program? (y/n): ")

print("The total price of the train tickets bought is $", ttprice)