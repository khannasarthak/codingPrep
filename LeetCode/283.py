# FASTEST:

class Solution(object):
    def moveZeroes(self, nums):
        noZero = 0
        for i in range(len(nums)):

            if nums[i]!=0:
                nums[noZero] = nums[i]
                noZero+=1

        for i in range(noZero,len(nums)):
            nums[i]=0

# SLOWER: like 2 pointers

# zero = 0  # records the position of "0"
#     for i in xrange(len(nums)):
#         if nums[i] != 0:
#             nums[i], nums[zero] = nums[zero], nums[i]
#             zero += 1
# # slowest

# for i in range(len(nums)):
# 	print ('CHANGE',nums)
# 	if nums[i]==0:
# 		print (nums[i])
# 		nums.append(nums.pop(i))
# 		print ('ITER:',i,nums)