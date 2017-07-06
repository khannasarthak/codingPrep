t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int, input().split()))
	op = []
	for i in range(1,len(a)):
		if a[i-1]>a[i]:
			op.append(a[i])
		else:
			op.append(-1)
	op.append(-1)
	print (*op)