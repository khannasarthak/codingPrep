t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	ma = a[0]
	mi = a[0]
	for i in range(1,n):
		tempmax = a[i]-i
		if tempmax>ma:
			ma = tempmax
		tempmin = a[i]-i
		if tempmin<mi:
			mi = tempmin
	print (ma-mi)