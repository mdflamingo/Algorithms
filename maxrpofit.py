"""
You are given an array prices where prices[i] is the price of a given stock
on the ith day.
You want to maximize your profit by choosing a single
day to buy one stock and choosing a different day in the
future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = []
        for ind, el in enumerate(prices):
            if ind != len(prices) - 1:
                if el <= prices[ind + 1]:
                    buy.append(el)
            else:
                buy.append(el)

        sell = max(prices[1:])
        t = min(buy[:-1])

        if t == buy[:-1]:
            return 0
        return sell - t


a = Solution()
print(a.maxProfit([7,6,4,3,1]))
