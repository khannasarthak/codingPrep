class Solution(object):
    def addStrings(self, num1, num2):
        if len(num1)>len(num2):
        # print ('num1')
            num2 = num2.zfill(len(num1))
        elif len(num1)<len(num2):
            num1 = num1.zfill(len(num2))


    # print (num1,num2)



        c = 0
        l = []
        for i,j in zip(num1[::-1],num2[::-1]):
            tmp = ord(i)-48 +ord(j)-48 +c
            if tmp>9:
                c=1 
                l.append(str(tmp%10))
            else:
                c=0
                l.append(str(tmp))
        if c!=0:
            l.append(str(c))
        return (''.join(l[::-1]))