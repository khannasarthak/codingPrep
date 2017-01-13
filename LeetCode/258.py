class Solution(object):
    def addDigits(self, num):
        while (len(str(num))!=1):
        	s = 0
        	for i in str(num):
        		s += int(i)
        	num = s
        return (num)
