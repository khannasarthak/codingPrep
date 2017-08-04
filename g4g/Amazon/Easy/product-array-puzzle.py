def prod(a):
	k = 1
	for i in a:
		k*=i
	return (int(k))

t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	op= []
	for i in range(len(a)):
		op.append(prod(a[:i] + a[(i + 1):]))
		
	print (*op)