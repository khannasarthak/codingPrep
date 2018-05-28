class Solution(object):
    def climbStairs(self, n):
        op = [1,2]

        for i in range(2,n):
            op.append(op[-1]+op[-2])
        return (op[n-1])