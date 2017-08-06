t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	
	for i in range(n-1):
		if i%2==0:
			if a[i]>a[i+1]:
				# print ('A',i)
				a[i],a[i+1]=a[i+1],a[i]
				# print (a)
		if i%2==1:	
			if a[i]<a[i+1]:
				# print ('B',i)
				a[i],a[i+1]=a[i+1],a[i]
				# print (a)
				
	print (*a)