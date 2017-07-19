# DO AGAIN IN O(n), current solution O(n^2)

t = int(input())
for p in (range(t)):
	n = input()
	a = list(map(int,(input().split())))
	b = list(map(int,(input().split())))
	op = {key: None for key in a}
	for i in op:
		k = 0
		for j in b:
			if i>=j:
				k +=1
		op[i] = k
	o = []
	for l in a:
		o.append(str(op[l]))
	print (','.join(o))