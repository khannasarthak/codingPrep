t = int(input())
for p in (range(t)):
	n = int(input())
	a = (bin(n)[2::])[::-1]
	op = 0
	for i in range(len(a)):
		op += int(a[i])*(5**(i+1))
	print (op)
		