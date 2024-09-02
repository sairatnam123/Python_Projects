"""
You are given an array of prices where prices[i] is the price of a
 given stock on an ith day.
 You want to maximize your profit by choosing a single day to buy
 one stock and choosing a different day in the future to sell that
 stock.
 Return the maximum profit you can achieve from this transaction.
 If you cannot achieve any profit, return 0
"""

import array


def maxProfit(prices):
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update the minimum price encountered so far
        if price < min_price:
            min_price = price

        # Calculate the profit if selling at the current price
        profit = price - min_price

        # Update the maximum profit if the current profit is greater
        if profit > max_profit:
            max_profit = profit

    return max_profit


#no of prices you want
length_of_list=int(input("Enter a number of prices:"))
list1=[]
for i in range(length_of_list):
    list1.append(int(input("enter a price per day")))
prices= array.array('i',list1)
maximum_profit=maxProfit(prices)
print("maximum profit for given prices",maximum_profit)

