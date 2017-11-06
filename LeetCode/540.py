# Need to do in O(logn)
class Solution(object):
    def singleNonDuplicate(self, nums):
        k = 0

        for i in nums:
            k=k^i
        return (k)