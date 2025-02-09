"""
src : https://leetcode.com/problems/longest-consecutive-sequence/description/
author : Seoyeon Kang
date : 08/02/2025
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums_set = set(nums)
        count = 0
        
        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1
                while num + length in nums_set:
                    length += 1
            
                count = max(count, length)
        
        return count
        