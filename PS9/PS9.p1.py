# Constants for month names
JAN, FEB, MAR = "Jan", "Feb", "Mar"
APR, MAY, JUN = "Apr", "May", "Jun"
JUL, AUG, SEP = "Jul", "Aug", "Sep"
OCT, NOV, DEC = "Oct", "Nov", "Dec"

def Fforepercent(month):
    if month in {JAN, FEB, MAR}:
        return 0.10
    elif month in {APR, MAY, JUN}:
        return 0.15
    elif month in {JUL, AUG, SEP}:
        return 0.20
    elif month in {OCT, NOV, DEC}:
        return 0.25
    else:
        raise ValueError("Invalid month")

def Fforecast(month, sales):
    nxtmthsales = sales * (1 + Fforepercent(month))
    return nxtmthsales

# Main
r = input("Do you want to forecast sales for next month? (y or n): ")
while r == "y":
    last_name = input("Enter the last name: ")
    month = input("Enter the month: ")
    sales = float(input("Enter the sales: "))
    print("The forecasted sales for next month is: ", Fforecast(month, sales))
    r = input("Do you want to forecast sales for next month? (y or n): ")
