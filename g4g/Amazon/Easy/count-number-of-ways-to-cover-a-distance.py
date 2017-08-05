t = int(input())
for p in (range(t)):
	a = int(input())
	op = [1,2,4]
	if a<=3:
		print (op[a-1])
	else:
		for i in range(3,a):
			op.append(op[i-1]+op[i-2]+op[i-3])
		print (op[-1])
