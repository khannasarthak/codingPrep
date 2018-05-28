class Solution(object):
    def convertToTitle(self, n):
        op = ''
        
        
        while n>0:
            r = n%26                              
            if r==0:                    
                op+='Z'
            if r!=0:                    
                op+= chr(r+64)
            n = (n-1)//26

        return (op[::-1])