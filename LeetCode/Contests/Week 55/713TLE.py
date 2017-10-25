class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        contiArray = []
        for i in range(len(nums)):
            for j in range(1,len(nums)-i+1):
                contiArray.append(nums[i:i+j])
        op = 0
        for i in contiArray:
            s = 1 
            for j in i:
                s*=j 
            if s<k:
                op+=1
        return (op)