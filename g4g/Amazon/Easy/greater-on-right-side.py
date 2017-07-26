# USING MAX

t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	op = []
	for i in range(len(a)-1):
		op.append(max(a[i+1:]))
	op.append(-1)
	print (*op)

# SECOND SOLUTION WITHOUT MAX 

t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	l = len(a)
	op = []
	maxr = a[-1]
	for i in range(l-2,-1,-1):
		tmp = a[i]
		a[i] = maxr
		if maxr<tmp:
			maxr = tmp
	a[-1] = -1
	print (*a)
