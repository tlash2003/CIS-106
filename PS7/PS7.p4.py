
f = open("C:\CIS106\Section 7\PS7.p4\PS7.P4 TEXT.txt", "r")

#initilize counters and sums
count = 0
tt_ext_price = 0.0

#get first data line
item = f.readline().rstrip('\n')
while item != "":
    qty = float(f.readline())
    price = float(f.readline())

    ext_price = qty * price

    tt_ext_price += ext_price
    count += 1

    print("Item: ", item)
    print("Quantity: ", qty)
    print("Price: ", price)
    print("Extended Price: ", ext_price)

    #get next data line
    item = f.readline().rstrip('\n')

    #close file

#final calculations
avg_ext_price = tt_ext_price / count

print("Total Extended Price: ", tt_ext_price)
print("Total Items: ", count)
print("Average Extended Price: ", avg_ext_price)
   
