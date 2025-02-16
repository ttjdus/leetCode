"""
src : https://leetcode.com/problems/longest-substring-without-repeating-characters/
author : Seoyeon Kang
date : 15/02/2025
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        ans = 1
        length = 1
        n = len(s)
        for i in range(n):
            seen = set()
            j = i
            while j < n:
                if s[j] in seen:
                    break
                seen.add(s[j])
                j += 1
            ans = max(ans, j - i)

        return ans