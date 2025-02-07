"""
src : https://leetcode.com/problems/product-of-array-except-self/description/
author : Seoyeon Kang
date : 07/02/2025
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n

        left = 1
        for i in range(n):
            ans[i] = left
            left *= nums[i]
            
        right = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]

        return ans