from collections import Counter
t = int(input())
for p in range(t):
	s1 = input()
	s2 = input()
	k = list(s1)
	n = list(s2)

	for i in n:
		k[:] = ([x for x in k if x != i])
		
	print (''.join(k))
