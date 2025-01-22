#input phase

item = input("Enter the item name: ")
quantity = int(input("Enter the quantity: "))

if item == "A":
    unit_price = 10
else:
    unit_price = 20

    ext_price = quantity * unit_price

#output phase

print("Item: ", item)
print("Unit Price: ", unit_price)
print("Extended Price: ", ext_price)