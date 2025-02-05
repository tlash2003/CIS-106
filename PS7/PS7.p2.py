# Initialize the first two numbers of the Fibonacci sequence
a = 1
b = 1
count = 20

# Print the first two numbers
print("The first 20 numbers in the Fibonacci sequence are:")
print(a)
print(b)

# Use a for loop to calculate and print the next numbers in the sequence
for _ in range(2, count):
    c = a + b
    print(c)
    a, b = b, c
