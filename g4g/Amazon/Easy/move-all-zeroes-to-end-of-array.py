t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	a = [x for x in a if x != 0]
	for i in range(n-len(a)):
		a.append(0)
	print (*a)