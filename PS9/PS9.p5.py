def Fvp(county):
    if county == "Cook":
        return 0.90
    elif county == "DuPage":
        return 0.80
    elif county == "McHenry":
        return 0.75
    elif county == "Kane":
        return 0.60
    else:
        return 0.70

def Favalue(mktvalue, county):
    assdvalue = mktvalue * Fvp(county)
    return assdvalue

# Main
ttlmktvalue = 0
ttlassdvalue = 0

r = input("Do you want to run the program? (y/n): ")
while r == "y":
    county = input("Enter the county: ")
    mktvalue = float(input("Enter the market value: "))
    assdvalue = Favalue(mktvalue, county)
    print("The market value is: ", mktvalue)
    print("The assessed value is: ", assdvalue)
    ttlmktvalue += mktvalue
    ttlassdvalue += assdvalue
    r = input("Do you want to run the program? (y/n): ")

print("The total market value is: ", ttlmktvalue)
print("The total assessed value is: ", ttlassdvalue)