
def fmpg (miles_trav,gallons):
    mpg = miles_trav/gallons
    return mpg

#main
count = 0

r = input ("Do you want to compute the miles per gallon? (y/n): ")
while r == 'y':
    dest = input("Enter the destination city: ")
    miles_trav = float(input("Enter the miles traveled: "))
    gallons = float(input("Enter the gallons of gas used: "))
    mpg = fmpg(miles_trav, gallons)
    count += 1
    print ("The destination city is: ", dest)
    print ("The miles traveled is: ", miles_trav)
    print ("The miles per gallon is: ", mpg)
    r = input("Do you want to compute the miles per gallon? (y/n): ")

print("The total number of entries is: ", count)