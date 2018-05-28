# SOlution 1
class Solution(object):
    def repeatedSubstringPattern(self, s):
        k=0
        for i in range(1,int(len(s)/2)+1):
            if ( s[:i]*((len(s))//i)) ==s:
                return True
            else:
                k=0
        if k==0:
            return False

# Solution 2
class Solution(object):
    def repeatedSubstringPattern(self, s):
        a = (s+s)[1:-1]
        return s in a
