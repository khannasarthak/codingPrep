class Solution(object):
    def findMaxAverage(self, nums, k):
        sumArray = [nums[0]]
        for i in range(1,len(nums)):
            # print (nums[i],nums[i-1])
            sumArray.append(nums[i]+sumArray[i-1])
        # print (sumArray)

        maxSum = float(sumArray[k-1])/ k
        for i in range(k,len(sumArray)):
            # print (i,i-k,sumArray[i-k],sumArray[i])
            # tmp =  (float(sumArray[k+i-1]-sumArray[i])/k)
            # if tmp>maxSum:
            # 	maxSum=tmp
            maxSum = max(maxSum,float(sumArray[i]-sumArray[i-k])/k)

        return (maxSum)