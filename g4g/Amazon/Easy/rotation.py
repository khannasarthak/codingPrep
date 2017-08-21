t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	m = a[0]
	for i in range(n):
		if (a[i:]+a[:i]) == sorted(a):
			print (i)