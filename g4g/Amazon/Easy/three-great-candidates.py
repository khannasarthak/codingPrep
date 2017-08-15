t = int(input())
for p in (range(t)):
	n = int(input())
	b = list(map(int,input().split()))
	b.sort()
	print (max((b[-1]*b[-2]*b[-3]),(b[0]*b[1]*b[-1])))