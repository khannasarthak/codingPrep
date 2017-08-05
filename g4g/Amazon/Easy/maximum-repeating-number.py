t = int(input())
for p in (range(t)):
	n,k = map(int,(input().split()))
	a = list(map(int, input().split()))
	c = [0]*k
	for i in range(n):
		c[a[i]]+=1
	print (c.index(max(c)))
	