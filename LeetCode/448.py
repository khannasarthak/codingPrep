class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = range(1,len(nums)+1)

        return (list(set(n)-set(nums)))