"""
src : https://leetcode.com/problems/longest-consecutive-sequence/description/
author : Seoyeon Kang
date : 11/02/2025
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        text = s.lower()
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', text)
        for i in range(len(clean_text)//2):
            if clean_text[i] != clean_text[len(clean_text) - i - 1]:
                return False
        
        return True