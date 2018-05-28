class Solution(object):
    def rob(self, nums):
        last,now = 0,0
        for i in nums:
            last,now = now,max(last+i,now)
        return now

# Need to see the solution and undestand DP properly