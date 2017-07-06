t = int(input())
for p in (range(t)):
	n = int(input())
	f = 0
	if n==1:
		f=1
	while (n!=1):
		if n%2==1:
			# print ('N',n)
			n = (n//2)
			# print ('R-',n%2)
			# print ('Q',n//2)
			f=1
		else:
			f=0
			print ('NO')
			break
	if f==1:
		print ('YES')