class Solution(object):
    def hammingDistance(self, x, y):
        binx = str(bin(x)[2:]).zfill(32)
        biny = str(bin(y)[2:]).zfill(32)
          
        h = 0
        for i,j in zip(binx,biny):
            if i!=j:
                h+=1 
        return (h)
        