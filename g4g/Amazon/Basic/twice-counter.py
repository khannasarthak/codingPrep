from collections import Counter
t = int(input())
for p in range(t):
	n = int(input())
	a = list(map(str, input().split()))
	k = Counter(a)
	w = 0
	for key in k:
		value = k[key]
		if value == 2:
			w += 1
	print (w)