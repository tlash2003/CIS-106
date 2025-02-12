
def compExtprice(qty, price):
    extprice = qty * price

    if extprice> 10000:
        discamnt = extprice * 0.1
    else:
        discamnt = 0

    newextprice = extprice - discamnt

    return newextprice


#Main

totalextprice = 0
r = input("Do you want to compute the extended price? (y/n): ")

while r == 'y':
    qty = float(input("Enter the quantity: "))
    price = float(input("Enter the price: "))
    extprice = compExtprice(qty, price)
    totalextprice += extprice
    print("The extended price is: ", extprice)
    r = input("Do you want to compute the extended price? (y/n): ")
     
print("The total extended price is: ", totalextprice)
