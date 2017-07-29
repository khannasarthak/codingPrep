import itertools
t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	l = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
	s =[]
	op =[]
	for i in a:
		s.append(l[i])
	for combination in itertools.product(*s):
		op.append((''.join(combination)))
	print (*op)
