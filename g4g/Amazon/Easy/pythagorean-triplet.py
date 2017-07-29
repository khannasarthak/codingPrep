def trip(a,n):
	for i in range(n):
		a[i] = a[i]**2
	a.sort()
	for i in range(n-1,1,-1):
		j=0
		k = i-1
		while(j<k):
			if a[j]+a[k]==a[i]:
				return 'Yes'
			else:
				if a[j]+a[k]<a[i]:
					j += 1 
				else:
					k-= 1 
	return 'No'
				
				
t = int(input())
for p in (range(t)):
	n = int(input())
	a =	list(map(int,input().split()))
	print (trip(a,n))
