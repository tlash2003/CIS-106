input_line = input("Enter a line of comma-separated values: ")

items = input_line.split(',')

# Print each item on a separate line, removing leading/trailing spaces
for item in items:
    print(item.strip())

