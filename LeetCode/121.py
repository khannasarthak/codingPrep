class Solution(object):
    def maxProfit(self, prices):
        minPrice = 9999999
        maxProfit = 0
        for i in range(len(prices)):
            profit = prices[i]-minPrice
            if prices[i]<minPrice:
                minPrice = prices[i]
            elif profit>maxProfit:
                maxProfit = profit

        return (maxProfit)