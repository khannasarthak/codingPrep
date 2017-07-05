def dist(a,b):
	return ((a[0]-b[0])**2 + (a[1] -b[1])**2)

t = int(input())
while (t!=0):
	a = ((input().split()))
	print (a)
	a = map(int,a)
	a = list(a)
	k = [a[i:i+2] for i in range(0, len(a), 2)]	# Very important, can use it in many many places
	p1 = k[0]
	p2 = k[1]
	p3 = k[2]
	p4 = k[3]
	d1 = dist(p1,p2)
	d2 = dist(p1,p3)
	d3 = dist(p1,p4)
	if (p1==p2==p3==p4):
		print (0)
	elif (d1==d2 and d2*2==d3):
		if (dist(p4,p2)==dist(p4,p3)):
			print (1)
	elif (d2==d3 and d3*2==d1):
		if (dist(p4,p2)==dist(p2,p3)):
			print (1)
	elif (d3==d1 and d1*2==d2):
		if (dist(p4,p3)==dist(p2,p3)):
			print (1)
	else:
		print (0)