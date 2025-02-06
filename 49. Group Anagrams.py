"""
src : https://leetcode.com/problems/group-anagrams/
author : Seoyeon Kang
date : 05/02/2025
"""

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grouped = defaultdict(list)

        for s in strs:
            # creating a key
            sorted_str = "".join(sorted(s))
            # grouping anagrams
            grouped[sorted_str].append(s)

        # return the value
        return list(grouped.values())