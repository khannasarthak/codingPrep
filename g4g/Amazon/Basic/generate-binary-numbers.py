t = int(input())
for p in range(t):
	n = int(input())
	a = []
	for i in range(1,n+1):
		a.append(bin(i)[2:])
	print (*a)