class Solution(object):
    def twoSum(self, nums, target):
        op = {}
        for i in range(len(nums)):
            comp = target-nums[i]
            if comp in op:
                return (op[comp],i)
            else:
                op[nums[i]]=i