class Solution(object):
    def checkPerfectNumber(self, num):
        if num<=0:
            return False
        s=[]
        for i in range(1,int(num**0.5)+1):
            if num%i==0:
                # print (i)
                s.append(i)
                if i!=num//i:
			        s.append(num//i)
                

        if num in s:
            return ((sum(s)-num)==num)
        return sum(s)==num