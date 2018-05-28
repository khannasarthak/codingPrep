from itertools import groupby
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        groups =[]
        for k,g in groupby(nums):
        	groups.append(list(g))
        return (sum(max(groups)))
