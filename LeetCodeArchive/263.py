class Solution(object):
    def isUgly(self, num):
        if num<=0:
	        return False

        for i in 2,3,5:
            while num%i==0:
                # print ('a',i)
                num=num/i

        # print (num)		
        return (num==1)