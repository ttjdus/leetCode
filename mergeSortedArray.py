"""
src : https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
author : Seoyeon Kang
date : 05/03/2025
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:]
        return nums1.sort()
