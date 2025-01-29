#initialize count and sum
count = 0
total = 0

#prompt user for input
r = input("Do you want to run program or not (Y or N)? ")
   
while r == 'Y' or r == 'y':
    #increment count
    count += 1
    last_name = input("Enter employee last name: ")
    no_hours = float(input("Enter number of hours worked: "))
    rate = float(input("Enter hourly pay rate:$"))

    if no_hours > 40:
        gross_pay = (40 * rate) + ((no_hours - 40) * rate * 1.5)
    else:
        gross_pay = no_hours * rate
   
    total = total + gross_pay

    print("Last Name: ", last_name)
    print("Gross pay : $ ", gross_pay)

    #prompt user for input
    r = input("Do you want to run program or not (Y or N)? ")

avg = total / count

print("Total gross pay:$ ", total)
print("Number of employees processed: ", count)
print("Average gross pay: $", avg)

