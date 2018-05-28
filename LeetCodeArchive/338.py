# Brute force
class Solution(object):
    def countBits(self, num):
        op = []
        for i in range(num+1):
            op.append(bin(i).count('1'))
        return (op)