class Solution(object):
    def missingNumber(self, nums):
        k = len(nums)
        return ((k*(k+1)/2) - sum(nums))

# solution is sum of n numbers - sum of numbers given in the input
