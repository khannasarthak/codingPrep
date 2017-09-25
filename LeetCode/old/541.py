class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)
        for i in range(0,len(s),2*k):
            r = s[i:i+k]
            s[i:i+k] = (r[::-1])
        return (''.join(s))