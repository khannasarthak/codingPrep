class Solution(object):
    def reverse(self, x):
        
        if x<0:
            
            k= int('-'+((str(x)[1:])[::-1]))
        else:
            k= int(str(x)[::-1])
        if k>2147483647 or k<-2147483647:
            return 0 
        return k