class Solution(object):
    def readBinaryWatch(self, num):
        
        op = []
        for h in range(12):
            for m in range(60):
                if (bin(h)+bin(m)).count('1')==num:
                    op.append('%d:%02d'% (h,m))

        return (op)