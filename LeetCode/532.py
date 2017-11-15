# set A & set B = common elements between them

from collections import Counter
class Solution(object):
    def findPairs(self, nums, k):
        if k>0:
            o = [n+k for n in nums]
            return (len((set(nums)&set(o))))

        elif k==0:
            return (sum(x>1 for x in Counter(nums).values()))
        return 0