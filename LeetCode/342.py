class Solution(object):
    def isPowerOfFour(self, num):
        import math
        if num>0:
            k = math.log10(num)/math.log10(4)
        else:
            return False
        return (k.is_integer())