#initialize  sum
sum = 0

#prompt user for input
r = input("Do you want to run program or not (Y or N)? ")
   
while r == 'Y' or r == 'y':
    qnty = int(input("Enter quantity: "))
    price = float(input("Enter price:$"))

    ext_price = qnty * price

    if ext_price > 10000.00:
       disc = 0.25
    else:
       disc = 0.10
   
    disc_amt = ext_price * disc
    total_price = ext_price - disc_amt

    sum = sum + disc_amt

    print ("The extended price is: $", ext_price)
    print ("The discount amount is: $", disc_amt)
    print ("The total price is: $", total_price)

    #prompt user for input 
    r = input("Do you want to run program or not (Y or N)? ")

print("Total discount amount:$ ", sum)





