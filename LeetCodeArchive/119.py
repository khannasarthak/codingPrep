class Solution(object):
    def getRow(self, rowIndex):        
            
        op = [[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(2,rowIndex+1):
            for j in range(1,i):
                op[i][j]=op[i-1][j-1]+op[i-1][j]

        return (op[rowIndex])