import time
start_time = time.time()
###############CODE STARRS##############
def func(a):
    for i in a:
        x = i[0]
        y = i[1]
        if x==y or x-2==y:
            if x%2==0:
                print(x+y)
            else:
                print(x+y-1)
        else:
            print ('No Number')
n = int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split(' '))))
(func(a))

###############CODE ENDS################
print("--- %s seconds ---" % (time.time() - start_time))
