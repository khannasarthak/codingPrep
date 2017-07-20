t = int(input())
for p in range(t):
	n = int(input())
	a = list(map(int,input().split()))
	c = {}
	t1 = 0
	t0 = 0
	t2 = 0
	for i in a:
		if i%3==0:
			t0 +=1
		c[0]=t0
		if i%3==1:
			t1 +=1
		c[1]=(t1)
		if i%3==2:
			t2+=1
		c[2]=(t2)
		
	## GROUP OF 2 
	s = 0
	s += (c[0]*(c[0]-1)/2)
	s += c[1]*c[2]
	 ## GROUP OF 3
	s += ((c[0] * (c[0]-1) * (c[0]-2))/6)
	s += ((c[1] * (c[1]-1) * (c[1]-2))/6)
	s +=  ((c[2]*(c[2]-1)*(c[2]-2))/6)
	s += c[0]*c[1]*c[2]
	print (int(s))