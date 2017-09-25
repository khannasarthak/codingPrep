class Solution(object):
    def isAnagram(self, s, t):
        a = s
        b  = t
        seta= set(a)
        setb= set(b)
        flag = 0
        if not a:
            if not b:
            	return (True)
            else:
                return (True)
        else:
        	if seta == setb:
        		for i in seta:
        			if a.count(i)==b.count(i):
        				flag = 1
        			else:
        				flag = 2
        				break
        	else:
        		flag = 2

        if flag == 1:
            return (True)
        elif flag ==2:
            return (False)
