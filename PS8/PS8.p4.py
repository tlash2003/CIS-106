def fpayrate(job_code):
    if job_code == 'L' or "l":
        return 25
    elif job_code == 'A' or "a":
        return 30
    elif job_code == 'J' or "j":
        return 50
    else:
        return 0

def fgrosspay(hours, job_code):
    if hours <= 40:
        grosspay = hours * fpayrate(job_code)
    else:
        grosspay = hours * fpayrate(job_code) + (hours - 40) * fpayrate(job_code) * 1.5
    return grosspay

# MAIN

ttlgrosspay = 0
r = input("Do you want to calculate gross pay? (y/n): ")
while r == 'y':
    last_name = input("Enter the last name: ").strip()
    hours = float(input("Enter the number of hours worked: "))
    job_code = input("Enter the job code (L, A, J): ")
    grosspay = fgrosspay(hours, job_code)
    ttlgrosspay += grosspay
    print("Last name: ", last_name)
    print("Gross pay: $", grosspay)
    r = input("Do you want to calculate gross pay? (y/n): ")
   
print("Total gross pay: $", ttlgrosspay)