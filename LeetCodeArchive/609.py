class Solution(object):
    def findDuplicate(self, paths):
        op = {}
        unique = 0
        for path in paths:
            tmp = path.split()
            unique+=len(tmp)-1
            for i in range(1,len(tmp)):
                content = ((tmp[i])[tmp[i].index('('):])
                # print (op)
                if content not in op:
                    
                    op[content]=[tmp[0]+'/'+(tmp[i])[:tmp[i].index('(')]]
                else:
                    # print ('asd')
                    s = tmp[0]+'/'+(tmp[i])[:tmp[i].index('(')]
                    # print (s)
                    op[content].append(s)
        dup = []
        if unique==len(op.values()):
            dup = []
        else:
            for i in op.values():
                if len(i)>1:
                    dup.append(i)
        return (dup)