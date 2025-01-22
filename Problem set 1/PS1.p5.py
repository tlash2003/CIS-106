price= float(input("Enter the price of the item: "))
discount_prct = float(input("Enter the discount percentage: "))

disc_amount = price * discount_prct 
discounted_price = price - disc_amount

print(f"Discount amount: {disc_amount}")
print(f"Discounted price: {discounted_price}")

