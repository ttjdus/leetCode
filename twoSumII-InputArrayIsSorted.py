"""
src : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
author : Seoyeon Kang
date : 11/02/2025
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1

        return []