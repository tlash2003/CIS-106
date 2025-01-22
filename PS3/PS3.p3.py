#input phase

num_of_books = int(input("Enter the number of books:"))
cost_of_book = float(input("Enter the cost of the book:$"))

# process phase

total_cost = num_of_books * cost_of_book

if total_cost > 50:
   shipping = 25
else:
   shipping = 0

# output phase
print("The total cost of the books is:$", total_cost)
print("The shipping cost is:$", shipping)
