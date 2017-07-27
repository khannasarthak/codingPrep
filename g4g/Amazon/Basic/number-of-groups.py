t = int(input())
for p in (range(t)):
	n = int(input())
	a = list(map(int,input().split()))
	op = 0
	c1 = c2 =c3 =0
	for i in a:
		if i%3==0:
			c1+=1 
		elif i%3==1:
			c2+= 1 
		elif i%3==2:
			c3 += 1 
	
	## GRoup of 2
	op += c2*c3
	op+= ((c1-1)*c1)/2
	
	## Groiup of 3 
	op += (c1*(c1-1)*(c1-2))/6
	op += (c2*(c2-1)*(c2-2))/6
	op += (c3*(c3-1)*(c3-2))/6
	op += c1*c2*c3 
	print (int(op))