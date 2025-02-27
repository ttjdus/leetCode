"""
src : https://leetcode.com/problems/koko-eating-bananas/
author : Seoyeon Kang
date : 27/02/2025
"""

import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left, right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2
            hours = sum(math.ceil(float(p) / mid) for p in piles)
            
            if hours <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1

        return res