# Get file
with open("C:\\CIS106\\Section 7\\PS7.p3\\PS7.P3.txt", "r") as file:
    # Initialize counters and sums
    ttl_bonus = 0.0

    # Get first data line
    last_name = file.readline().rstrip('\n')
    item = last_name  # Initialize item to enter the loop
    while item != "":
        salary = float(file.readline().rstrip('\n'))

        if salary > 100000:
            rate = 0.2
        elif salary > 50000:
            rate = 0.15
        else:
            rate = 0.1

        bonus = salary * rate
        ttl_bonus += bonus

        print("Last Name: ", last_name)
        print("Salary: ", salary)
        print("Bonus: ", bonus)

        # Get next data line
        last_name = file.readline().rstrip('\n')
        item = last_name  # Update item to check for loop continuation

# Final calculations
print("The total amount given as bonus: ", ttl_bonus)