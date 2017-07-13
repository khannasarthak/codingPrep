t = int(input())
for p in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	m = max(a)
	asc = sorted(a)
	dsc = sorted(a,reverse =True)
	if a == asc:
		print (m,1)
	elif a == dsc:
		print (m,2)
	else:
		for i in range(1,len(a)):
			k= (a[i:]+a[:i])
			if (k)==asc:
				print (m,4)
			elif (k)==dsc:
				print (m,3)