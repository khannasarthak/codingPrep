class Solution(object):
    def getSum(self, a, b):
        m = 2**32 # Max value
        n = -2**32 # Min value
        
        while(b!=0):
            if b==m:
                return (a^n)
            c = a& b
            a = a^b
            b = c<<1
            
        return a