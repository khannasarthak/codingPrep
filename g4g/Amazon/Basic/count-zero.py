t = int(input())
for p in range(t):
	n = int(input())
	k = 0
	for i in range(1,n+1):
		k +=  (9*(10**(i-1)-9**(i-1)))
	print (k)