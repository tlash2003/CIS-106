#input phase
stocksticksymbol = input("Enter the stock stick symbol:")
num_of_shares = float(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))

#process phase
amount_invested = num_of_shares * cost_per_share

#output phase
print("Amount invested: $", amount_invested)
