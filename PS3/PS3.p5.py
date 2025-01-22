#input phase

last_name = input("Enter the last name: ")
no_of_dep = int(input("Enter the number of dependents: "))
gross_income = float(input("Enter the gross income: "))

#process phase
adj_gross_inc = gross_income - (12000 * no_of_dep)

if adj_gross_inc > 50000:
    tax_rate = 0.2
else:
    tax_rate = 0.1

inc_tax = adj_gross_inc * tax_rate
if inc_tax < 0:
    inc_tax = 100

#output phase

print("The last name is: ", last_name)
print("The gross income is:$", gross_income)
print("The number of dependents is:", no_of_dep)
print("The adjusted gross income is:$", adj_gross_inc)
print("The income tax is:$", inc_tax)
