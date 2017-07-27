import math
t = int(input())
for p in (range(t)):
	n = int(input())
	if n==2:
		print ('4')
	else:
		print (math.ceil(n*n/2))