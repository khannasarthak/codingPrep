class Solution(object):
    def isHappy(self, n):
        for j in range(0,10):
        	k = 0
        	for i in str(n):
        		k=k+ (int(i)**2)
        	#print (k)
        	n = k
        if (k==1):
        	return (True)
        else:
        	return (False)
