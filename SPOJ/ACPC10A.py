import time
start_time = time.time()
###############CODE STARRS##############
def func(a):
    for i in a[1:-1]:
        if (i[1]-i[0])==(i[2]-i[1]):
            print ('AP',i[2]+(i[2]-i[1]))
        elif (i[1]/i[0])==(i[2]/i[1]):
            print ('GP',int(i[2]*(i[2]/i[1])))





a=[[1,1,1]]
b = []
while (a[-1]!=[0,0,0]):
    b = (list(map(int,input().split(' '))))
    # print (b)
    a.append(b)
    # print ('-1', a[-1])
# print ('a-',a)
(func(a))

###############CODE ENDS################
print("--- %s seconds ---" % (time.time() - start_time))
