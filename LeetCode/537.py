class Solution(object):
    def complexNumberMultiply(self, a, b):
        op=[]
        a = a.split('+')
        b = b.split('+')

        t1 = (int(a[0])*int(b[0]))

        t2 = (int(a[0])*int(b[1][:-1]))

        t3 = (int(a[1][:-1])*int(b[0]))

        t4 = -1*(int(a[1][:-1])*int(b[1][:-1]))

        op=[str(t1+t4),'+',str(t2+t3),'i']
        return (''.join(op))