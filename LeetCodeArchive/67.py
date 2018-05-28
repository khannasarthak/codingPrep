class Solution(object):
    def addBinary(self, a, b):
        if len(b)>len(a):
            a = a.zfill(len(b))
        elif len(b)<len(a):
            b = b.zfill(len(a))
        c = 0 
        op = []
        for i, j in zip(a[::-1],b[::-1]):
            k = int(i)+int(j)+c
            if k>1:
                op.append(str(k%2))
                c=1
            else:
                op.append(str(k))
                c=0
        if c!=0:
            op.append(str(c))
        return (''.join(op)[::-1])