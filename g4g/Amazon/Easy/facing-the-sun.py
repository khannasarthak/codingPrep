t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	c = 1
	mx = a[0]
	for i in range(1,n):
		if a[i]>mx:
			c+=1
			mx = a[i]
	print (c)