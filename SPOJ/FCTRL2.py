import time

start_time = time.time()
###############CODE STARRS##############
import math
def fact(a):
    for i in a:
        print (math.factorial(i))


n = int(input())
a=[]
for i in range(n):
    a.append(int(input()))
fact(a)
# print ('final...',fact(a))

###############CODE ENDS################
print("--- %s seconds ---" % (time.time() - start_time))
