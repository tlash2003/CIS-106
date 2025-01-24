
#input phase
num_tick= int(input("Enter the number of tickets: "))

#process phase
if num_tick >= 25:
    pptick = 50
elif num_tick >= 10:
    pptick = 60
elif num_tick >= 5:
    pptick = 70
else:
    pptick = 75

total_cost = num_tick * pptick

#output phase
print("The number of tickets is:", num_tick)
print("The price per ticket is:$", pptick)
print("The total cost of the tickets is:$", total_cost)