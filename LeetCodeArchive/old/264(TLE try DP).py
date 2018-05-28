class Solution(object):
    def nthUglyNumber(self, n):
        def isUgly(num):
            if num<=0:
                return False
            for i in [2,3,5]:
                while num%i==0:
                    num = num/i
            return (num==1)
        count = 1
        i=1
        while (count<n):
            
            i += 1
            if isUgly(i):
                count += 1
        return (i)
# TLE, need to find a faster solution
# Try with dynamic programming later