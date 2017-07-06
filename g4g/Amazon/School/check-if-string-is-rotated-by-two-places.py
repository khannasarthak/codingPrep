t = int(input())
while (t!=0):
	t -= 1
	k = input()
	a = input()
	rot = [-2,-1,1,2]
	f=0
	for i in rot:
		if (a[i:]+a[:i]==k):	# rotating sting
			f=1
	print (f)