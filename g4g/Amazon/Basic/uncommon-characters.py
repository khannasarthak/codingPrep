t = int(input())
for p in (range(t)):
	a = input()
	b = input()
	k1 = [item for item in b if item not in a] # to check if items of b not in a
	k2 = [item for item in a if item not in b]
	b = (list(set(k1).union(set(k2))))
	b.sort()
	print (''.join(b))
