class Solution(object):
    def findUnsortedSubarray(self, nums):
        check = sorted(nums)
        
        if check == nums:
            return 0
        a = []
        for i in range(len(nums)):
            if nums[i]!=check[i]:
                a.append(i)
        op = nums[a[0]:a[-1]+1]
        return (len(op))