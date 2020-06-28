""" 
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times)."""

def maxProfit(prices):
    # Check empty 
    if len(prices) == 0:
        return 0 
     
    first = prices[0]   # set starting price
    profit = 0          # Set the initial profit
    
    for i in range(1, len(prices)):
        if prices[i] > first:
            profit += prices[i] - first
        first = prices[i]

    return profit

def max_profit(prices):
    # Check empty 
    if len(prices) == 0:
        return 0 
     
    first = prices[0]   # set starting price
    profit = 0          # Set the initial profit

    for i in range(1, len(prices)):
        # Compare prices to check for profit
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]     # Sum up if there is a profit

    return profit          

print(maxProfit([4, 3, 3, 6, 2, 1]))

print(max_profit([4, 3, 3, 6, 2, 1]))
