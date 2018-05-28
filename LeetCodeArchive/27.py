class Solution(object):
    def removeElement(self, nums, val):  
        for i in range(nums.count(val)):
            nums.pop(nums.index(val))
        return (len(nums))