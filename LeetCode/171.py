class Solution(object):
    def titleToNumber(self, s):
        op = 0
        power = len(s)-1
        for i in s[:-1]:
            print (i)
            op+= ((ord(i)-64)*26**power)
            print (op,power)
            power-=1

        op += ord(s[-1])-64

        return (op)