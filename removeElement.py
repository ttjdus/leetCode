"""
src : https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-%20interview-150
author : Seoyeon Kang
date : 08/03/2025
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        
        return len(nums)