name = input("Enter your full name (Firstname Lastname): ").strip()

# 
parts = name.split()

# Check if the input is valid
if len(parts) != 2:
    print("Invalid input. Please enter exactly one first name and one last name.")
else:
    fname, lname = parts
    # Print the name in the desired format
    print(f"{lname}, {fname[0]}.")
