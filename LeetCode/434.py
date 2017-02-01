class Solution(object):
    def countSegments(self, s):
        a = s.split()
        if a:
            return len(a)
        else:
            return 0
