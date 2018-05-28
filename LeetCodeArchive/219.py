class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        n = {}
        for i in range(len(nums)):
            if nums[i] in n and i - n[nums[i]] <= k :
                return True
            n[nums[i]]=i
        return False