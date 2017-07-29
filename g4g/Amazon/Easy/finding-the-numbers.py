from collections import Counter
t = int(input())
for p in (range(t)):
	n = int(input())
	arr =	input().split()
	c = Counter(arr)
	op = []
	for i in c:
		if c[i]%2==1:
			op.append(int(i))
	op.sort()
	print (*op)