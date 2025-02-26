"""
src : https://leetcode.com/problems/search-a-2d-matrix/description/
author : Seoyeon Kang
date : 26/02/2025
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
