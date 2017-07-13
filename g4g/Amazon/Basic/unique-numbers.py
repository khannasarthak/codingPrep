t = int(input())
for p in range(t):
	n,m = map(int,(input().split()))
	a = [x for x in range(n,m+1)]
	op = []
	for i in a:
		# print ((int((''.join(list(set(str(i))))))))
		# if i == int((''.join(list(set(str(i)))))):
		# 	print (i)
		if len(str(i)) == (len(set(str(i)))):
			op.append(i)
	print (*op)