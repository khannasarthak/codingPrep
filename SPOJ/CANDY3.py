import time
start_time = time.time()
###############CODE STARRS##############


t = int(input())
final =[]
for i in range(t):
    a=[]
    space = input()
    n = int(input())#students
    for j in range(n):
        a.append(int(input()))
    if (sum(a)%n==0):
        final.append('YES')
    else:
        final.append('NO')

for i in final:
    print (i,sep='\n')





###############CODE ENDS################
print("--- %s seconds ---" % (time.time() - start_time))
