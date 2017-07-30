t = int(input())
for p in (range(t)):
	n = int(input())
	a =	list(map(int,input().split()))
	s1 = sum(a)
	if n==1:
		print (n)
	else:
		s2=0
		for i in range(n):
			s1 -= a[i]
			if s2 == s1:
				print (i+1)
				break
			elif s2>s1:
				print (-1)				
				break
			s2 += a[i]

