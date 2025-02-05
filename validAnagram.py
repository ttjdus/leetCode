"""
src : https://leetcode.com/problems/valid-anagram/
author : Seoyeon Kang
date : 05/02/2025
"""

from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)
        