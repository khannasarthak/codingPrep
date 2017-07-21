t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	k = 0
	if 1 not in a:
		print ('-1')
	else:
		for i in a:
			if i ==1:
				break
			k += 1
		print (k)
	