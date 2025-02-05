#initialize zeros
c= 0
accum_interest = 0


principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the rate of interest: "))


for count in range (1, 6):   
    interest = principle * rate
    end_bal = principle + interest
    accum_interest = accum_interest + interest
    print(format(count, '1d'),format(principle, '10.2f'),format(end_bal, '10.2f')) 
    principle = end_bal

print ("The total interest is ", accum_interest)
