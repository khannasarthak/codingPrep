from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        c = Counter(s)
        numEven = 0
        numOdd =0
        # print (c)
        for i in c:
            if c[i]%2==0:
                numEven+=c[i]
            elif c[i]%2==1 and c[i]>1:
                numOdd+=c[i]-1
        if numEven==len(s):
            return (len(s))
        else:
            return (numEven+1+numOdd)