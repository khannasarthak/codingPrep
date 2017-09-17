class Solution(object):
    def matrixReshape(self, nums, r, c):
        if r*c != len(nums)*len(nums[0]):
            return (nums)    
        data = []
        for i in nums:
            data += i

        i = 0
        op=[]
        while i<len(data):
            op.append(data[i:i+c])
            i+=c
        return (op)