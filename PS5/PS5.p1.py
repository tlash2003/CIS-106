# input phase

widgqty = int(input("Enter the quantity of widgets: "))

#processing phase

if widgqty > 10000:
   price = 10
elif 5000 <= widgqty <= 10000:
   price = 20
else :
   price = 30

extprice = widgqty * price
tax = extprice * .07
total = extprice + tax

#output phase

print ("The extended price is:$", extprice)
print ("The tax is:$", tax)
print ("The total is:$", total)

