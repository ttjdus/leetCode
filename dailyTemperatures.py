"""
src : https://leetcode.com/problems/daily-temperatures/description/
author : Seoyeon Kang
date : 24/02/2025
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(temperatures)
        answer = [0]*n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pop_index = stack.pop()
                answer[pop_index] = i - pop_index

            stack.append(i)
        
        return answer
