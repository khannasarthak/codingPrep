class Solution(object):
    def constructRectangle(self, area):
        mid = int(area**0.5)
        while (mid>0):
            if area%mid == 0:
                return (int(area/mid),int(mid))
            mid -= 1