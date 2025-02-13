def Favgs(s1,s2,s3,handicap):
    avgscore = (s1+s2+s3)/3
    avgh = (avgscore+handicap)/3
    return avgscore,avgh

#MAIN
lname = input("Enter last name: ")
s1 = int(input("Enter score 1: "))
s2 = int(input("Enter score 2: "))
s3 = int(input("Enter score 3: "))
handicap = int(input("Enter handicap: "))
avgscore,avgh = Favgs(s1,s2,s3,handicap)
print("Last name: ",lname)
print("Average score: ",avgscore)
print("Average score with handicap: ",avgh)

