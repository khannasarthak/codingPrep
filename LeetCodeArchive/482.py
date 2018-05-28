class Solution(object):
    def licenseKeyFormatting(self, S, K):
        tmp = ''
        for i in S:
            if i.isalnum():
                tmp+=i.upper()
        tmp = tmp[::-1]
        op = ''
        for i in range(0,len(tmp),K):
            op+=tmp[i:i+K]+'-'
        op = op[::-1]
        return (op[1:])