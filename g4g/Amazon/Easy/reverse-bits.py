t = int(input())
for p in range(t):
	n = int(input())
	b = str(format(n,'b'))
	b = b.zfill(32)
	print (int(b[::-1],2))
