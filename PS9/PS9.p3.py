from doctest import OutputChecker

def Fpercentoff(make, model, code):
    if make == "Honda" and model == "Accord":
        return 0.10
    elif make == "Toyota" and model == "Rav4":
        return 0.15
    elif code == "Y" or code == "y":
        return 0.20
    else:
        return 0.05

def Fprice(Fpercentoff, MSRP):
    newMSRP = MSRP - (MSRP * Fpercentoff)
    tax = newMSRP * 0.07
    outprice = newMSRP + tax
    return outprice

# MAIN
ttlMSRP = 0
ttlsales = 0

r = input("Do you want to calculate Out the Door Price? (Y/N): ")
while r.lower() == "y":
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    code = input("Enter the code of the car: ")
    MSRP = float(input("Enter the MSRP of the car: $"))
    price = Fprice(Fpercentoff(make, model, code), MSRP)
    print("The suggested out the door price is:$",price)
    ttlMSRP += MSRP
    ttlsales += price
    r = input("Do you want to calculate Out the Door Price? (Y/N): ")

print("Total MSRP: $", ttlMSRP)
print("Total Sales: $", ttlsales)