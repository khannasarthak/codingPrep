t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	c = 0
	for i in range(0,n):
		for j in range(i,n):
			if a[i]>a[j]:
				c += 1
	print (c)