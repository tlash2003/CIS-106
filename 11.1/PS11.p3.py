def display_names(lnames, scores):
    for i in range(len(lnames)):
        print(f"{lnames[i]} scored {scores[i]}")

def hilow(lnames, scores):
    l = len(scores)
    hiscore = -1.0
    lowscore = 999999999.9
    high_index = -1
    low_index = -1

    for y in range(l):
        if float(scores[y]) > hiscore:
            hiscore = float(scores[y])
            high_index = y
        if float(scores[y]) < lowscore:
            lowscore = float(scores[y])
            low_index = y

    print(f"Highest score is {lnames[high_index]} with a score of {hiscore}")
    print(f"Lowest score is {lnames[low_index]} with a score of {lowscore}")

# Define arrays
lastn = []
scores = []

# Read data from file
with open('C:\\CIS106\\Section 11\\TextFile1.txt', 'r') as f:
    lnames = f.readline().strip()

    while lnames != "":
        lastn.append(lnames)
        s = f.readline().strip()
        scores.append(s)
        lnames = f.readline().strip()

# Display names and scores
display_names(lastn, scores)

# Find and display highest and lowest scores
hilow(lastn, scores)
