t = int(input())
while (t!=0):
	t -= 1
	n,p = map(int,(input().split()))
	nums = list(map(int,(input().split())))
	f=0
	for i in nums:
		for j in nums:
			if i*j==p:
				f = 1
	if f==1:
		print ("Yes")
	else:
		print ('No')

# Try to do it in less than n^2