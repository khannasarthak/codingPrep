a = int(input())
c = []
for i in range(a):
	c.append(input())
for b in c:
	blen = len(b)//2

	half = b[:blen]
	new = []
	for k in range(blen):
		if k%2==0:
			new.append(half[k])
	print (''.join(new))
