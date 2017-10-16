class Solution(object):
    def calPoints(self, ops):
        c = 0
        valid =[]

        for i in range(len(ops)):

            if (ops[i].lstrip("-").isdigit()):
                # print (ops[i])
                c+=int(ops[i])
                valid.append(int(ops[i]))


            elif ops[i]=='C':
                c-=valid.pop()

            elif ops[i]=='D':
                # print ('last double',valid[-1])
                c += (valid[-1]*2)
                valid.append(int(valid[-1]*2))
            elif ops[i]=='+':
                k = valid[-1]+valid[-2]
                c+= k 
                valid.append(int(k))
            # print  (ops[i],'--VALID--',valid,'--C--',c)

        return c