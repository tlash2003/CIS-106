#initialize count
count = 0

#prompt user for input
r = input("Do you want to run program or not (Y or N)? ")
   
while r == 'Y' or r == 'y':
    #increment count
    count += 1
    last_name = input("Enter your last name: ")
    ex_one = int(input("Enter your first exam score: "))
    ex_two = int(input("Enter your second exam score: "))

    avg = (int(ex_one) + int(ex_two)) / 2

    print("Last Name: ", last_name)
    print("Average exam score : ", avg)
    #prompt user for input
    r = input("Do you want to run program or not (Y or N)? ")

print("Number of students processed: ", count)

