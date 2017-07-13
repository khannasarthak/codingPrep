t = int(input())
for p in range(t):
	s = (input())
	s = s.lower()
	op = []
	two = ['a','b','c']
	three = ['d','e','f']
	four = ['g','h','i']
	five = ['j','k','l']
	six = ['m','n','o']
	seven = ['p','q','r','s']
	eight =  ['t','u','v']
	nine = ['w','x','y','z']
	for i in s:
		if i in two:
			op.append(2)
		elif i in three:
			op.append(3)
		elif i in four:
			op.append(4)
		elif i in five:
			op.append(5)
		elif i in six:
			op.append(6)
		elif i in seven:
			op.append(7)
		elif i in eight:
			op.append(8)
		elif i in nine:
			op.append(9)
	op = map(str,op)
	print (''.join(op))