class Solution(object):
    def isPowerOfFour(self, num):
        import math
        if num>0:

            b = math.log(num,4)
            return (b.is_integer())
        else:
            return (False)
