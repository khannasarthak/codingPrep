class Solution(object):
    def isPowerOfTwo(self, n):
        if bin(n).count('1')==1 and n>0:
            return True
        return False