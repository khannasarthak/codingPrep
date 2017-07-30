t = int(input())
for p in (range(t)):
	a = input()
	N=0
	E=1
	S=2
	W=3
	current = N
	x=0
	y=0
	for i in a:
		if i =='R':
			current =(current+1)%4
		elif i=='L':
			current=(current+4-1)%4
		else:
			if current == N:
				y+=1 
			elif current== E:
				x+=1 
			elif current==W:
				x-=1 
			else:
				y-=1
	if x==0 and y==0:
		print ('Circular')
	else:
		print ('Not Circular')