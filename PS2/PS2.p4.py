
#input phase
make = input ("Enter car make: ")
model = input ("Enter car model: ")
msrp_amount = float(input("Enter msrp amount: "))
disct_prct = float(input("Enter discount percent: "))

#processing phase
off_msrp = msrp_amount * disct_prct
disctd_price = msrp_amount - off_msrp

#output phase
print("Make:", make)
print("Model:", model)
print("Msrp:", msrp_amount)
print("Discounted price:", disct_prct)
print("Amount off msrp:", off_msrp)
print("Discounted price:",disctd_price)