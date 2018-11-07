import time
start_time = time.time()
###############CODE STARRS##############
n = -1
op = list()
while True:    # infinite loop
    n = int(input())
    if n == -1:
        break  # stops the loop
    else:
        a=[]
        for i in range(n):
            a.append(int(input()))
        # print (a)
        if sum(a)%n==0:
            avg = int(sum(a)/len(a))
            c=0
            for num in a:
                if num>avg:
                    c+= (num-avg)
            op.append(c)
            # print ('c--',c)
            # print (op)
        else:
            op.append(-1)
# print ('OP---',op)
for i in op:
    print (i)

###############CODE ENDS################
print("--- %s seconds ---" % (time.time() - start_time))

#test