t = int(input())
for p in (range(t)):
	n,x = map(int,input().split())
	a = list(map(int,input().split()))
	f = 0
	
	for i in a:
		# print (i,abs(x-i))
		if ((x-i)) in a:
			f=1
			break
		else:
			f=0
	if f==1:
		print ('Yes')
	else:
		print ('No')