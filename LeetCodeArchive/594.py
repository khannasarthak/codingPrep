from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        c =Counter(nums)
        op = 0
        for x in c:
            if x+1 in c:
                op = max(op,c[x]+c[x+1])
        return (op)