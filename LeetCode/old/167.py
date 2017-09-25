class Solution(object):
    def twoSum(self, numbers, target):
        # BINARY SEARCH : Understand this properly today
        for i in range(0,len(numbers)):
            first,last = i+1,len(numbers)-1
            tmp = target - numbers[i]
            while first<=last:
                mid = first + (last-first)//2
                if numbers[mid] == tmp:
                    return (i+1, mid+1)
                elif numbers[mid]<tmp:
                    first = mid+1
                else:
                    last = mid-1

# Another solution : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/#/discuss, check the dictionary method.