class Solution(object):
    
    def convertToBase7(self, num):
        if num==0:
            return '0'
        op = ''
        n = abs(num)
        while n:
            op += str(n%7)
            n = n//7

        if num>0:
            return op[::-1]
        else:
            return '-'+op[::-1]