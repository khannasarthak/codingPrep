from collections import Counter

def isUnique(s):
	flag = False
	c = Counter(s)
	for i in c:
		if c[i]>1:
			flag =  False
		else:
			flag = True
	return flag