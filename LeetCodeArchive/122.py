class Solution(object):
    def maxProfit(self, prices):
        s = prices
        op = 0
        for i in range(1,len(s)):
            # print (i)
            if (s[i]-s[i-1])>0: # profit
                # print (s[i-1]-s[i])
                op+= (s[i-1]-s[i])
        return (abs(op))