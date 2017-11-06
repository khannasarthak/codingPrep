from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        c = Counter(nums)
        op = []
        for i in c:
            if c[i]==1:
                op.append(i)
        return op