"""
src : https://leetcode.com/problems/3sum/
author : Seoyeon Kang
date : 12/02/2025
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    # Remove duplicate
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results