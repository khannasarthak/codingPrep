t = int(input())
for p in (range(t)):
	n = int(input())
	a =	list(map(int,input().split()))
	b =	list(map(int,input().split()))
	op = []
	while a and b:
		if a[0]<b[0]:
			op.append(a.pop(0))
		else:
			op.append(b.pop(0))
	print (op[int(2*(n-1)/2)]+op[int(2*(n-1)/2)+1])

# PYTHONIC SOLUTION FASTER IN ALL RUNS

op = a+b
	op.sort()
	print (op[int(2*(n-1)/2)]+op[int(2*(n-1)/2)+1])