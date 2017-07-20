import math
t = int(input())
for p in range(t):
	n = int(input())
	f = 0
	if n==1:
		f=1
	else:
		for x in range(2,int(n**0.5)+1):
			k = math.log10(n)/math.log10(x)
			if (k).is_integer():
				f = 1
				break
			else:
				f = 0
	print (f)