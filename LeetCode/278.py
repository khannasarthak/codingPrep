class Solution(object):
    def firstBadVersion(self, n):
        h = n
        l = 0
        while l<h:
            m = int((l+h)/2)
            if isBadVersion(m):
                h = m
            else:
                l = m+1
        return l
        