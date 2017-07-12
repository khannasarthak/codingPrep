t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	b = (sorted(a))
	mini=100000
	for i in range(0,len(b)-1):
		m = b[i+1]-b[i]
		# print (m)
		if (m<mini):
			mini = m
	print (mini)