class Solution(object):
    def romanToInt(self, s):
        c = {'I':1,'V':5,'X':10,'C':100,'D':500,'M':1000,'L':50}
        op = 0
        for i in range(len(s)-1):
            if c[s[i]]<c[s[i+1]]:
                op-=c[s[i]]
            else:
                op+=c[s[i]]

        return (op+c[s[-1]])