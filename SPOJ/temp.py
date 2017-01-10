import time
start_time = time.time()
###############CODE STARRS##############
t = int(input())
op = []
for i in range(t):
    n = int(input())
    m =list(map(int,input().split(' ')))
    w =list(map(int,input().split(' ')))
    m.sort()
    w.sort()
    hot = []
    op.append(sum(a*b for a,b in zip(m,w)))
for i in op:
    print (i,sep='\n')


###############CODE ENDS################
print("--- %s seconds ---" % (time.time() - start_time))
