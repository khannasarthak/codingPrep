t = int(input())
for p in (range(t)):
	n,m,x = map(int,input().split())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	op = []
	a.sort()
	b.sort()
	for i in a:
		for j in b:
			if i+j==x:
				k = (' '  +str(i)+' '+str(j))
				op.append(k)
	if len(op)==0:
		print (-1)
	else:
		print (','.join(op))