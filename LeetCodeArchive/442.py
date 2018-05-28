from collections import Counter
class Solution(object):
    def findDuplicates(self, nums):
        op = []
        c = Counter(nums)
        for i in c:
            if c[i]==2:
                op.append(i)
        return op