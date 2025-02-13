def Ffootage(length,width,height):
    sqfootage = (2 * length * width)+ (2 * length * height )+ (2 * width * height )
    return sqfootage

#MAIN

r = input("Do you want to run the program? (y/n): ")
while r == "y":
    l = float(input("Enter the length of the room: "))
    w = float(input("Enter the width of the room: "))
    h = float(input("Enter the height of the room: "))
    gallons = Ffootage(l,w,h)/50
    print("The number of gallons needed to paint the room is:", gallons)
    r = input("Do you want to run the program again? (y/n): ")
