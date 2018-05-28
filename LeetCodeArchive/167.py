class Solution(object):
    def twoSum(self, numbers, target):
        # numbers = [2,3,4]
        tmp = {}
        for i,num in enumerate(numbers):
            if target-num in tmp:
                return (tmp[target-num]+1,i+1)
            else:
                tmp[num]=i

# Hashmap faster than binary           

# Binary Saerch 

# for i in range(len(numbers)):
#             l = 1
#             r = len(numbers)-1
#             chk = target - numbers[i]
#             while l<=r:
#                 m = l +(r-l)//2
#                 if numbers[m]==chk:
#                     return (i+1,m+1)

#                 elif numbers[m]<chk:
#                     l = m+1 
#                 else:
#                     r = m-1   