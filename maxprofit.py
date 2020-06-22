""" 
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times)."""

def maxProfit(prices):
    # empty list
    if len(prices) == 0:
        return 0 
    j = 0
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i- 1]:
            profit += prices[i] - prices[i - 1]
        
    return profit
                

maxProfit([1, 3, 2, 6, 2, 1])
