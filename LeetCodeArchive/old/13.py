class Solution(object):
    def romanToInt(self, s):
        v = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        op = 0 
        for i in range(0,len(s)-1):
            if v[s[i]]<v[s[i+1]]:

                op = op-v[s[i]]

            else:
                op = op+v[s[i]]
        return (op+v[s[-1]])

 # SECONDARY SOLUTION
 #        def rtod(n):
 #            op = 0
 #            for i in range(0,len(n)):
 #            # if s[i] == 'I' and s[-1] == 'X':
 #            # 	op = op+ 9
 #                if s[i] =='I':
 #                    op=op+1
 #                elif s[i]=='V':
 #                    op = op+5
 #                elif s[i]=='X':
 #                    op = op+10
 #                elif s[i]=='L':
 #                    op = op+50
 #                elif s[i]=='C':
 #                    op = op+100
 #                elif s[i]=='D':
 #                    op = op+500
 #                elif s[i]=='M':
 #                    op = op+1000
 #            return op
 #        # print (rtod(s))
 #        op = rtod(s)
 #        if s.find('CM')!=-1:
 #            # print ('CM')
 #            op = op -200
 #        if s.find('IX')!=-1:
 #            # print ('IX')
 #            op = op - 2
 #        if s.find('XC')!=-1:
 #            # print ('XC')
 #            op = op - 20
 #        if s.find('XL')!=-1:
	# # print ('XC')
 #            op = op - 20
 #        if s.find('IV')!=-1:
 #            op = op - 2
 #        if s.find('CD')!=-1:            
 #            op = op -200
 #        return (op)