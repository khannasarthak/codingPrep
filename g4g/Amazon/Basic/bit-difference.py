t = int(input())
for p in (range(t)):
	a,b = (map(int,input().split()))
	a1 = str(format(a,'08b'))
	b1 = str(format(b,'08b'))
	a1 = a1.zfill(20)
	b1 = b1.zfill(20)
	c = 0
	for i,j in zip(a1,b1):
		if i!=j:
			c += 1
	print (c)
