t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	o = []
	for i in range(0,len(a)):
		if (i+1)==a[i]:
			o.append(a[i])
	if o==[]:
		print ('Not Found')
	else:
		print (*o)

# Re DO with bianry search
# http://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/