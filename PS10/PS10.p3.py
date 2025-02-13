def Fcommission(sales):
    if sales > 100000:
       commission = 0.1 * sales
    else:
        commission = 0.05 * sales

    nxtyr = 0.05 * sales
    return commission, nxtyr

#MAIN
lname = input("Enter last name: ")
sales = float(input("Enter sales: "))

commission, nxtyr = Fcommission(sales)
print("Salesperson: ", lname)
print("Commission: ", commission)
print("Next year's target: ", nxtyr)
