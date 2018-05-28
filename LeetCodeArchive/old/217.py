class Solution(object):
    def containsDuplicate(self, nums):
        # if not nums:
        #     return False
        # print (sorted(nums), (list(sorted(set(nums)))))
        if sorted(nums)==list(sorted(set(nums))):

            return False
        else:
            return True
