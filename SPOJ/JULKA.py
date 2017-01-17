import time
start_time = time.time()
###############CODE STARRS##############
k=[]
n = []
for i in range(10):
    total = int(input())
    more = int(input())
    print((total -int((total-more)/2)))
    print(int((total-more)/2))



###############CODE ENDS################
print("--- %s seconds ---" % (time.time() - start_time))
