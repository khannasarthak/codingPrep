from collections import Counter
t = int(input())
for p in (range(t)):
	n = int(input())
	a = input()
	c = Counter(a)
	k = ''
	for i in a:
		if (c[i]==1):
			k = k + str(i)
			break
	if k !='':
		print (k)
	else:
		print ('-1')