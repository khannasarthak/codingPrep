import math
from collections import Counter
class Solution(object):
    def majorityElement(self, nums):        
        n = int(math.floor(len(nums)/2))
        count = Counter(nums)
        k= (count.most_common()[0])
        if k[1]>n:
            return (k[0])
