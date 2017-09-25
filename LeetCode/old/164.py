class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2:
            return 0
        else:
            return (max([j-i for i, j in zip((sorted(nums))[:-1], (sorted(nums))[1:])]))
