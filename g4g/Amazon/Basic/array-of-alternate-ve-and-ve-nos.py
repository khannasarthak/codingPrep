t = int(input())
for p in (range(t)):
	a = input()
	n = list(map(int,(input().split())))
	neg = []
	pos = []
	tot = []
	for i in n:
		if i>=0:
			pos.append(int(i))
		else:
			neg.append(int(i))
	for i,j in zip(pos,neg):
		tot.append(i)
		tot.append(j)
	if len(neg)>len(pos):
		tot = tot + neg[len(pos):]
	elif len(neg)<len(pos):
		tot = tot + pos[len(neg):]
	print (*tot)