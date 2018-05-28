class Solution(object):
    def convertToTitle(self, n):
        op = ''
        while n!=0:
            op+= (chr(((n-1)%26)+ord('A')))
            n = (n-1)//26

        return (op[::-1])
        """