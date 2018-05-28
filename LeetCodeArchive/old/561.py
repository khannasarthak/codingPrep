class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        # a = list(zip(*(iter(nums),) * 2))
        # k = 0
        # for i in a:
        # # 	print (i)
        # 	k = k + min(i)
        # return (k)
        return (sum(nums[::2]))


## ALTERNATE SOLU: minimum number will be the odd numners. Therefore, return (sum(nums[::2]))