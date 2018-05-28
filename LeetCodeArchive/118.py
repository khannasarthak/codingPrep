class Solution(object):
    def generate(self, numRows):
        op = [[1]*i for i in range(1,numRows+1)]
        for i in range(2,numRows):
            for j in range(1,i):
                op[i][j]=op[i-1][j-1]+op[i-1][j]
        return op