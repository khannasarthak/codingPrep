import time
start_time = time.time()
###############CODE STARRS##############
def func(a):
    for i in a:
        a = i[0]
        b = i[1]

        if b ==0:
            print ('1')
        else:
            b = b%4
            a = a%10
            if b==0:
                b=4

            print ((a**b)%10)

a= []
n = int(input())
for i in range(n):
    a.append(list(map(int,input().split(' '))))
func(a)



###############CODE ENDS################
print("--- %s seconds ---" % (time.time() - start_time))
