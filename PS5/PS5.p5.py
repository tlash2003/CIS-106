#input phase

last_name = input("Enter employee last name: ")
salary = float(input("Enter employee salary:$ "))
job_level = int(input("Enter employee job level: "))

#process phase
if job_level >= 10:
   rate = 0.25
elif job_level >= 5:
   rate = 0.20
else:
    rate = 0.10

bonus = salary * rate

#output phase

print("Employee: ", last_name)
print("Bonus: $", bonus)