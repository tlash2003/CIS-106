def ftuition(hours, code):
    if code == "I" or code == "i":
        tuition = hours * 250
    elif code == "O" or code == "o":
        tuition = hours * 550
    else:
        tuition = 0
  
    return tuition

# MAIN

ttltuition = 0

r = input("Do you want to calculate tuition? (y/n): ")
while r == "y" or r == "Y":
    last_name = input("Enter the student last name: ")
    hours = int(input("Enter the number of credit hours: "))
    code = input("Enter the code (I or O): ")
    tuition = ftuition(hours, code)
    print("Last Name: ", last_name)
    print("Tuition: $", tuition)
    ttltuition = ttltuition + tuition
    r = input("Do you want to calculate tuition? (y/n): ")

print("Total tuition: $", ttltuition)
