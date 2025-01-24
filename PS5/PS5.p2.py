
#input phase

part_no = input("Enter the part number: ")
qnty = int(input("Enter the quantity: "))

#process phase
if part_no == "10" or "55":
   unit_cost = 1.00
elif part_no == "99":
   unit_cost = 2.00
elif part_no == "70" or "80":
   unit_cost = 3.00
else:
   unit_cost = 5.00

total_cost = qnty * unit_cost

#output phase
print("The part number is: ", part_no)
print("The unit cost is:$", unit_cost)
print("The total cost is:$", total_cost)