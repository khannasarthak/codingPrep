t = int(input())
for p in (range(t)):
	a = int(input())
	if a==0:
		print (0)
	else:
		k =  ((format((a),'b')))
		print ((str(k)[::-1].index('1'))+1)