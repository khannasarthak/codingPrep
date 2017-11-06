from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        return zip(*Counter(nums).most_common(k))[0]