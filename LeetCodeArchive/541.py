class Solution(object):
    
    def reverseStr(self, s, k):
        s = list(s)
        for i in range(0,len(s),2*k):
            # if len(s[i:k+i])<k:
            s[i:k+i] = reversed(s[i:k+i])
            # else:
            # 	s[i:k+i] = (s[i:k+i:-1])

        return (''.join(s))