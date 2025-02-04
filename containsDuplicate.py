"""
src : https://leetcode.com/problems/contains-duplicate/
author : Seoyeon Kang
date : 04/02/2025
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        exist = set()
        for i in nums:
            if i in exist:
                return True
            else: 
                exist.add(i)
        return False