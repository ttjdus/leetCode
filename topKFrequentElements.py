from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: in t
        :rtype: List[int]
        """
        count_items = Counter(nums)
        frequent_items = count_items.most_common(n=k)

        return [num for num, _ in frequent_items]
        