#input phase

quantity = int(input("Enter the quantity of the item: "))

#processing phase

if quantity >= 1000:
   unit_price = 3.00
else:
   unit_price = 5.00

ext_price = quantity * unit_price

tax = ext_price * 0.07

total_price = ext_price + tax

#output phase

print ("The quantity is: ", quantity)
print ("The unit price is: ", unit_price)
print ("The extended price is: ", ext_price)
print ("The tax is: ", tax)
print ("The total price is: ", total_price)

