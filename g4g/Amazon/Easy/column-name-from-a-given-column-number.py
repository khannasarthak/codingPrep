t = int(input())
for p in (range(t)):
	a = int(input())
	op = []
	while (a>0):
		r = a%26
		if r==0:
			op.append('Z')
			a = int(a/26)-1
		else:
			op.append(chr((r-1)+ord('A')))
			a = int(a/26)
	print ((''.join(op))[::-1])