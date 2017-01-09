# Takes too long to run, need to make it faster.
import time
start_time = time.time()
###############CODE STARRS##############
# def findPrime(a): #SIEVE OF EROSTHANES
#     for i in a:
#         start = i[0]
#         end = i[1]
#         sqend = int(i[1]**0.5)
#         # print (start,end)
#         # nums = list(range(start,end))
#         A = [True]*end
#         A[0]=A[1]=False
#         print ('First',A)
#         # print (len(A))
#         for j in range(2,sqend+1):
#             if A[j]:
#                 for k in range(j*j,end,j):
#                     # print (k)
#                     A[k] = False
#         print (A)
#         for num in range(len(A)):
#             if A[num]==True and num>=start:
#                 print (num)

def sieve(start,end):
    multiples = set()
    for i in range(2, end+1):
        if i not in multiples:
            if i>=start:
                yield i     # uses less memory
            multiples.update(range(i*i, end+1, i))

n = int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split(' '))))
for i in a:
    primes = sieve(i[0],i[1])
    for x in list(primes):
        print (x,sep='\n')
    print ()



###############CODE ENDS################
print("--- %s seconds ---" % (time.time() - start_time))
