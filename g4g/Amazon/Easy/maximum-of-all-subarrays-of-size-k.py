t = int(input())
for p in (range(t)):
	n,k = map(int,(input().split()))
	a = list(map(int,input().split()))
	op= []
	for i in range(n-k+1):
		op.append(max(a[i:i+k]))
	print (*op)