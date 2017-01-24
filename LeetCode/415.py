class Solution(object):
    def addStrings(self, num1, num2):
        inta = 0
        intb = 0

        for c in num1:
        	inta =inta*10 +(ord(c) - ord('0'))
        for c in num2:
        	intb =intb*10 +(ord(c) - ord('0'))



        return (str(inta+intb))
