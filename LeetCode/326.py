class Solution(object):
    def isPowerOfThree(self, n):
        import math
        if n>0:
            return ((math.log10(n)/math.log10(3)).is_integer())
        return False