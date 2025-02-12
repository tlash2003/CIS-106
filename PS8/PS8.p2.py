from itertools import count


def batavg(hits, atbats):
    batavg = hits/atbats
    return batavg


#Main

count = 0
r = input("Do you want to compute the batting average? (y/n): ")

while r == 'y':
    last_name = input("Enter the player's last name: ")
    hits = float(input("Enter the number of hits: "))
    atbats = float(input("Enter the number of at bats: "))
    avg = batavg(hits, atbats)
    count += 1
    print("The player's last name is: ", last_name)
    print("The batting average is: ", avg)
    r = input("Do you want to compute the batting average? (y/n): ")

print("The total number of players is: ", count)