class Solution(object):
    def constructRectangle(self, area):
        k = int(area**0.5)
        while (k>0):
            if area%k==0 and int(area%k)!=k:
                return (int(area/k),k)
            k = k-1pront 