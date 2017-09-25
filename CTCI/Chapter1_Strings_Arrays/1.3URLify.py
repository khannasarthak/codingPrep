def url(a):
	k = a.split()
	op = []
	for i in k:
		if i!=' ':
			op.append(i)
	return '%20'.join(op)

print ((url(a)))