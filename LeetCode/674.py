class Solution(object):
    def findLengthOfLCIS(self, nums):
        i=0 
        tmp = 0
        while i<len(nums):
            # print (i,i+1)
            conti=1
            while i+1<len(nums) and nums[i]<nums[i+1]:
                i +=1 
                conti+=1 
            tmp = max(tmp,conti)
            i+=1 
        return (tmp)