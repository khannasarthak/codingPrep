class Solution(object):
    def firstUniqChar(self, s):
        c = {}
        op=[]
        for i in s:
            if i in c:
                c[i]+=1
            else:
                c[i]=1
        # print (c)
        
        for i in c:
            if c[i]==1:
                op.append(s.index(i))
        # print (op)
        if len(op)==0:
            return -1
        return (min(op))