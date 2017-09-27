class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        nums = ''.join(list(map(str,nums)))
        return (len(max(nums.split('0'))))