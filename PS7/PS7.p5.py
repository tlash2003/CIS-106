
# Get file
f = open("C:\\CIS106\\Section 7\\PS7.p5\\PS7.P5.txt", "r") 

# Initialize counters and sums
count = 0
total_tuition = 0

# Get first data line
last_name = f.readline().rstrip('\n')
print(last_name)
while last_name != "":
     code = (f.readline().rstrip('\n'))
     credit_hours = int(f.readline().rstrip('\n'))

     if code == "i" or code == "I":
        cost_per_credit = 250.00
     else:
        cost_per_credit = 500.00

     tuition = credit_hours * cost_per_credit
     count += 1
     total_tuition += tuition

     print("Student Last Name: ", last_name)
     print("No of credits taken: ", credit_hours)
     print("Cost of tuition: ", tuition)

     # Get next data line
     last_name = f.readline().rstrip('\n')
        
# Close file
f.close()


print("Total number of students: ", count)
print("Total tuition owed: ", total_tuition)


