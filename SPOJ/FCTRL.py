import time
start_time = time.time()
###############CODE STARRS##############
def fact(a):
    for n in a:
        c = 0
        while n >= 5:
            n //= 5
            c += n
            
        print (c)
n = int(input())
a=[]
for i in range(n):
    a.append(int(input()))
fact(a)
# print ('final...',fact(a))

###############CODE ENDS################
print("--- %s seconds ---" % (time.time() - start_time))
