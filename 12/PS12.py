
# 1. Prompt the user for a number which will represent the number of items in a list.
#num_items = int(input("Enter the number of items in the list: "))
#items_list = []

#for i in range(num_items):
    #item = int(input(f"Enter item {i+1}: "))
    #items_list.append(item)

#print("List after adding items:", items_list)

# 2. Insert the score of 99 at position 1 within the list.
#.insert(1, 99)
#print("List after inserting 99 at position 1:", items_list)

# 3. Replace the value of 99 with the value 100. 
#index_99 = items_list.index(99)
#items_list[index_99] = 100
#print("List after replacing 99 with 100:", items_list)

# 4. Create a second list  Display this list.
#second_list = [500, 600, 700, 800, 900]
#print("Second list:", second_list)

# Extend the first list with this second list. 
#items_list.extend(second_list)
#print("First list after extending with second list:", items_list)

# 5. Remove the value 800 from the first list. 
#items_list.remove(800)
#print("First list after removing 800:", items_list)

# 6. Remove the third item from the first list.
#del items_list[2]
#print("First list after removing the third item:", items_list)

# 7. Create a list of grades
#grades = ["A", "B", "C", "A", "A", "C"]

# 8. Display a count of the number of A grades.
#count_A = grades.count("A")
#print("Number of A grades:", count_A)

# 9. Display the index (position) of the first B grade.
#index_B = grades.index("B")
#print("Index of the first B grade:", index_B)

# 10. Look for grade of F in the grades list. 
#if "F" not in grades:
    #print("F is not in the list")

# 11. Clear (but do not delete) the second list of integers. Display the list.
#second_list.clear()
#print("Second list after clearing:", second_list)

# 12. Delete the second list. Try to display it. 
#del second_list
#try:
    #print(second_list)
#except NameError:
    #print("Second list no longer exists")

# 13. Create a list of players 
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]

# 14. Sort 
print("Sorted list of players:", players)

# 15. Make a copy of the list 
players2 = players.copy()
print("Copy of the list of players (players2):", players2)

# 16. Reverse the order 
players2.reverse()
print("Original list of players:", players)
print("Reversed list of players2:", players2)
