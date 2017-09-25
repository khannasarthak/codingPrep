from collections import Counter

a = 'azAZ'

def pp(s):
	s = s.lower()
	s = ''.join(s.split())
	c = Counter(s)
	f = False
	count = 0
	for i in c:
		if c[i]%2==1:
			count+=1
	if count==1 or count==0:
		f = True
	# print (count)
	return f



print (pp(a))

