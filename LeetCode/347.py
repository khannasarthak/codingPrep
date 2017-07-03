from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):       
        count = Counter(nums)
        return ((zip(*count.most_common(k)))[0]) 


# zip function could be used to extract the first item from the tuple. 
# Eg: nums = [1,1,1,2,2,2,3,3,3], k = 3
# count.most_common(k) gives [(1, 3), (2, 3), (3, 3)]
# list(zip(*count.most_common(k))) gives [(1, 2, 3), (3, 3, 3)], keys in first list and values in second list
# list(zip(*count.most_common(k)))[0] gives just the first list of keys, ie. (1,2,3)