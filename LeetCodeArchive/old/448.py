class Solution(object):
    def findDisappearedNumbers(self, nums):
        # print (set(nums))
        # print (max(nums))
        if not nums:
            return nums
        else:
            a = set(list(range(1,len(nums)+1)))
            b = set(nums)
            deff = (a-b)
            print (list(deff))
            return (list(deff))
