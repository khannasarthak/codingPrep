class Solution(object):
    def findRelativeRanks(self, nums):
        keys = sorted(nums,reverse=True)
# print (keys)
        values = ["Gold Medal", "Silver Medal", "Bronze Medal"]+[str(x) for x in range(4,len(nums)+1)]

        op = dict(zip(keys,values))
        return (list(map(op.get,nums)))