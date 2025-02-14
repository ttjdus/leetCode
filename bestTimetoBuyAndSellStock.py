"""
src : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
author : Seoyeon Kang
date : 14/02/2025
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

