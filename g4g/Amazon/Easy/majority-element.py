from collections import Counter
t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	c = Counter(a)
	f = 0
	for i in c:
		if c[i]>int(n/2):
			print (i)
			f = 0
			break
		else:
			f = 1
	if f==1:
		print ('NO Majority Element')