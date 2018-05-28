from collections import Counter

# Solution using Moore's voting Algo
# O(n) and O(1) space
# Hashing is slow for this
class Solution(object):
    def majorityElement(self, nums):
        count = 0
        major = nums[0]
        for i in range((len(nums))):
            if count==0:
                count+=1
                major = nums[i]
            elif major==nums[i]:
                count +=1
            else:
                count-=1
        return (major)
