def Fdisc(qtty,price,discrate):
    extprice = qtty*price
    discamnt = extprice*discrate
    discdprice = extprice-discamnt
    return discdprice,discamnt

#MAIN
qtty = int(input("Enter quantity: "))
price = float(input("Enter price:$ "))
discrate = float(input("Enter discount rate: "))
discdprice,discamnt = Fdisc(qtty,price,discrate)
print("The quantity bought is: ",qtty)
print("The price is:$ ",price)
print("Discount amount:$ ",discamnt)
print("Discounted price:$ ",discdprice)

