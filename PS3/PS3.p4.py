
#input phase

app_name = input("Enter the appliance name: ")
app_cost = float(input("Enter the cost of the appliance: "))

#process phase

if app_cost > 1000:
    warrantee = 0.1 * app_cost
else:
    warrantee = 0.05 * app_cost

total_cost = app_cost + warrantee

#output phase
print("The appliance name is: ", app_name)
print("The cost of the appliance is: ", app_cost)
print("The warrantee cost is: ", warrantee)
print("The total cost is: ", total_cost)
