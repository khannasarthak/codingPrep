def primes(n):
	op = []
	for num in range(1,n):
	    if all(num%i!=0 for i in range(2,int((num**0.5))+1)):
	       op.append(int(num))
	return (op)
	   
		
t = int(input())
for p in range(t):
	n = int(input())
	k = (primes(n))
	a =  (k[1:])
	b = a
	op= []
	for i in a:
		for j in b:
			if i*j<=n:
				op.append(i)
				op.append(j)
	print (*op)
	