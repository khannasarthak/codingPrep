# SOLUTION 1: USING HASH [SLOW]

# from collections import Counter
# class Solution(object):
#     def singleNumber(self, nums):
#         c = Counter(nums)
#         for i in c:
#             if c[i]==1:
#                 return (i)


# SOLUTION 2: USING BIT MANIPULATION [FAST]
# a XOR a = 0, a XOR b XOR a = b 

class Solution(object):
    def singleNumber(self, nums):
        op = 0
        for i in nums:
            op = op^i
        return (op)