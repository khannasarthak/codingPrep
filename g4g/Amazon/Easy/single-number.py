t = int(input())
for p in range(t):
	n = int(input())
	a = list(map(int,input().split()))
	a.sort()
	k = a[0]
	for i in a[1:]:
		k = k^i
	print (k)