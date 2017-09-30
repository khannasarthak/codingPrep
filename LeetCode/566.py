class Solution(object):
    def matrixReshape(self, nums, r, c):
        op = []
        tmp = []

        if r*c!=len(nums)*len(nums[0]):
            return nums
        else:
            for i in nums:
                for j in i:
                    tmp.append(j)



            for i in range(0,len(tmp),c):
                op.append(tmp[i:i+c])
            return (op)
