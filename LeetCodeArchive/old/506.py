class Solution(object):
    def findRelativeRanks(self, nums):        
        key = sorted(nums,reverse=True)
        value = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str,range(4,len(nums)+1)))
        dik = dict(zip(key,value))
        return (list(map(dik.get, nums)))