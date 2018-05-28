class Solution(object):
    def countBits(self, num):
        s = []
        for i in range(num+1):
        	(s.append((bin(i)[2:]).count('1')))
        return (s)
