class Solution(object):
    def nextGreaterElement(self,findNums, nums):
        op = []
        for i in range(len(findNums)):

            k = nums.index(findNums[i])
            # print (nums[i],'IN',findNums,'J',k)

            for j in range(k,len(nums)):
                # print (j)
                if findNums[i]<nums[j]:
                    op.append(nums[j])
                    break

            else:
                op.append(-1)
        return (op)