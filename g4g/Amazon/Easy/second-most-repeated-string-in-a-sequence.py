from collections import Counter
t = int(input())
for p in (range(t)):
	n = int(input())
	a =	input().split()
	c = Counter(a)
	k=(c.most_common(2)[1])[0]
	print (k)