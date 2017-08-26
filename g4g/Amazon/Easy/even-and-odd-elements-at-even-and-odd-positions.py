t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	even = []
	odd = []
	op= []
	for i in a:
		if i%2==0:
			even.append(i)
		elif i%2==1:
			odd.append(i)
	for i,j in zip(even,odd):
		op.append(i)
		op.append(j)
	# print (len(op),op)
	if len(even)>len(odd):
		# print (even[len(odd):])	
		op = op + even[len(odd):]
	elif len(even)<len(odd):
		# print (odd[len(even):])
		op = op + odd[len(even):]
	print (*op)