class Solution(object):
    def findComplement(self, num):
        op = ''

        for i in bin(num)[2:]:
            if i=='1':
                op+='0'
            elif i=='0':
                op+='1'
        return (int(op,2))