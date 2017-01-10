import time
start_time = time.time()
###############CODE STARRS##############
def func(a):
    for i in a:
        op = []
        operator = []
        precedence = ['+','-','*','/','^']
        opPre = {'+':1,'-':1,'*':2,'/':2,'^':3}
        print (opPre)
        for char in i:
            if char.isalpha():
                op.append(char)
                print (op)
            elif char in precedence:
                operator.append(char)
                print (operator)

                out = op + operator[::-1]
        print (out)




n = int(input())
a=[]
for i in range(n):
    a.append(list(map(str,input())))
(func(a))

###############CODE ENDS################
print("--- %s seconds ---" % (time.time() - start_time))
