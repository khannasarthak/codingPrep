class Solution(object):
    def countPrimes(self, n):
        
        if n<3:
            return 0
        primes = [True]*n

        primes[0]=primes[1]=False
        # print (primes)

        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i,n,i):
                    primes[j]=False

        return (sum(primes))