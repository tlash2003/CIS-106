#input phase

prncpl = float(input("Enter the principal amount: "))
years = int(input("Enter the number of years to maturity: "))

#processing phase
if prncpl > 100000 and years == 5:
    rate = 0.06
elif 50000 <= prncpl<= 100000 and years == 10:
    rate = 0.05
elif 50000 <= prncpl<= 100000 and years == 5:
    rate = 0.04
else:
    rate = 0.02

interest = prncpl * rate * years

#output phase
print("The principal amount is:$ ", prncpl)
print("The interest rate is: ", rate)
print("The interest amount is:$",interest)