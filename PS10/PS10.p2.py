def Fpoints(ex1,ex2,ex3):
    ttlpoints = ex1 + ex2 + ex3
    avg = ttlpoints/3
    return ttlpoints, avg

#MAIN
last_name = input("Enter last name: ")
ex1 = int(input("Enter points for exam 1: "))
ex2 = int(input("Enter points for exam 2: "))
ex3 = int(input("Enter points for exam 3: "))

ttlpoints, avg = Fpoints(ex1,ex2,ex3)

print("the student last name is: ", last_name)
print("The total points are: ", ttlpoints)
print("The average points are: ", avg)

