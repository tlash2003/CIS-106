
#define global variables
total = 0
tax = 0

def Fcomps(qtty,price):
    total = qtty * price
    tax = total *0.07
    return total, tax

#MAIN
qtty = int(input("Enter the quantity of the item: "))
price = float(input("Enter the unit price of the item:$ "))
total, tax = Fcomps(qtty, price)
print("The total cost is $", total)
print("The tax is $", tax)