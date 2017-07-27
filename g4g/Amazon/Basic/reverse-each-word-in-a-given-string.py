t = int(input())
for p in (range(t)):
	a = input().split('.')
	op = []
	for i in a:
		op.append(i[::-1])
	print ('.'.join(op))