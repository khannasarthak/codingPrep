class Solution(object):
    def isHappy(self, n):
        c = 0
        while (n!=1):
            if c>20:
                break
            c+=1
            
            k = list(str(n))
            s = 0
            for i in k:
                s += int(i)**2
            n = s

        if n==1:
            return True
        return False