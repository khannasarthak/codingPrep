class Solution(object):
    def lexicalOrder(self, n):
        b=[]
        for i in range(1,n+1):
            b.append(i)
        a = list(b)
        a.sort(key=str)
        return (a)
