class Solution(object):
    def plusOne(self, digits):
        k = ''.join(list(map(str,digits)))
        # print (k)
        n = int(k)+1        
        return (list(map(int,str(n))))