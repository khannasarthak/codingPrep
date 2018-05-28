class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        poison = duration	# from last element
        for i in range(len(timeSeries)-1):
            if (timeSeries[i]+duration-1)<timeSeries[i+1]:
                poison+=duration
            elif (timeSeries[i]+duration-1)>=timeSeries[i+1]:
                poison+=timeSeries[i+1]-timeSeries[i]
        return (poison)