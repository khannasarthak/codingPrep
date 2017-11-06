class Solution(object):
    def judgeSquareSum(self, c):
        for i in range(int(c**0.5)+1):
            if ((c-i**2)**0.5).is_integer():
                return True
        return False