import time
start_time = time.time()
###############CODE STARRS##############
t = int(input())
s = []
for i in range(t):
    a = int(input())
    s.append((a-1)*250+192)
for i in s:
    print (i)




###############CODE ENDS################
print("--- %s seconds ---" % (time.time() - start_time))
