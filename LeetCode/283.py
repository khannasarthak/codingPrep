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

# i = 0
# k = 0
# while (i<len(nums)):
	
# 	if k==len(nums)-1:
# 		break
# 	if nums[i]==0:
# 		nums.append(nums.pop(i))
# 		print ('ITER:',i,nums)
# 		i=i 
# 		k+=1
# 	else:
# 		i+=1
# 		k+=1

# slowest

# for i in range(len(nums)):
# 	print ('CHANGE',nums)
# 	if nums[i]==0:
# 		print (nums[i])
# 		nums.append(nums.pop(i))
# 		print ('ITER:',i,nums)