t = int(input())
for p in (range(t)):
	a = int(input())
	op = [1,2]
	for i in range(2,a):
		op.append(op[-1]+op[-2])
	print (op[-1])