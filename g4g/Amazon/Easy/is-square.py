def dist(x1,y1,x2,y2):
	return int((x1-x2)**2+(y1-y2)**2)
	

t = int(input())
for p in (range(t)):
	x1, y1, x2, y2, x3, y3, x4, y4 = map(int,input().split())
	d1 = dist(x1,y1,x2,y2)
	d2 = dist(x1,y1,x3,y3)
	d3 = dist(x1,y1,x4,y4)
	if d1==d2 and d3 == 2* d1 and d1!=0:
		print ('Yes')
	elif d2==d3 and d1 == 2* d2 and d2!=0:
		print ('Yes')
	elif d3==d1 and d2 == 2* d3 and d3!=0:
		print ('Yes')
	else:
		print ('No')