# time limit exceeded, need to use hashing maybe?

class Solution(object):
    def longestConsecutive(self, nums):
        ans =0
        for i in range(len(nums)):
        	if nums[i]-1 not in nums:

        		j = nums[i]
        		while (j in nums):
        			j+=1
        		ans=max(ans, j-nums[i])
        return (ans)
