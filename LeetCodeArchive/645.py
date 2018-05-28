class Solution(object):
    def findErrorNums(self, nums):
        
        # ums = [1,2,2,4]
        count = [0 for x in range(len(nums)+1)]

        # print (count)

        for i in range(len(nums)):
            if count[nums[i]] ==0:

                count[nums[i]]=1
            else:
                # print ('-')
                count[nums[i]]+=1
        # print (count)

        dup = count.index(2)
        missing = count[1:].index(0)+1
        return ([dup,missing])