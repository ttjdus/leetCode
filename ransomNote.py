"""
src : https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
author : Seoyeon Kang
date : 06/03/2025
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_count = Counter(magazine)
        for char in ransomNote:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        
        return True
